import requests
import pandas as pd
from datetime import datetime
from typing import Dict, Optional
import os
import bcchapi
from .mindicador import get_currency_values as get_mindicador_values

# Credenciales del Banco Central (mantenidas como respaldo)
BCCH_EMAIL = "ma.maripangue@duocuc.cl"
BCCH_PASSWORD = "Matiasyoung25"

def get_bcch_values() -> Dict[str, float]:
    """
    Obtiene los valores actuales de UF y USD desde el Banco Central de Chile
    Returns:
        Dict con los valores de UF y USD
    """
    try:
        # Inicializar cliente del Banco Central
        client = bcchapi.Siete(BCCH_EMAIL, BCCH_PASSWORD)
        
        # Obtener valores de UF
        uf_data = client.cuadro(
            series=['F073.UFF.PRE.Z.D'],  # Código serie UF
            fechaDesde='2024-01-01',
            fechaHasta='2024-12-31',
            primeraFecha='2024-01-01',
            ultimaFecha='2024-12-31',
            observado=True
        )
        
        # Obtener valores de USD
        usd_data = client.cuadro(
            series=['F073.TCO.PRE.Z.D'],  # Código serie USD
            fechaDesde='2024-01-01',
            fechaHasta='2024-12-31',
            primeraFecha='2024-01-01',
            ultimaFecha='2024-12-31',
            observado=True
        )
        
        # Convertir a DataFrame para facilitar el manejo
        uf_df = pd.DataFrame(uf_data)
        usd_df = pd.DataFrame(usd_data)
        
        # Obtener el último valor disponible
        uf_value = float(uf_df.iloc[-1]['valor'])
        usd_value = float(usd_df.iloc[-1]['valor'])
        
        return {
            'uf': uf_value,
            'usd': usd_value
        }
    except Exception as e:
        print(f"Error al obtener valores de monedas desde BCCH: {e}")
        return None

def get_currency_values() -> Dict[str, float]:
    """
    Obtiene los valores actuales de UF y USD, intentando primero con mindicador.cl
    y usando el Banco Central como respaldo
    Returns:
        Dict con los valores de UF y USD
    """
    # Intentar primero con mindicador
    values = get_mindicador_values()
    
    # Si mindicador falla, intentar con Banco Central
    if values is None:
        values = get_bcch_values()
    
    # Si ambos fallan, usar valores por defecto
    if values is None:
        print("Usando valores por defecto debido a errores en las APIs")
        values = {
            'uf': 38000.0,  # Valor por defecto UF
            'usd': 950.0    # Valor por defecto USD
        }
    
    return values

def convert_to_uf(clp_amount: float) -> float:
    """
    Convierte un monto en CLP a UF
    """
    values = get_currency_values()
    return clp_amount / values['uf']

def convert_to_usd(clp_amount: float) -> float:
    """
    Convierte un monto en CLP a USD
    """
    values = get_currency_values()
    return clp_amount / values['usd']

def format_currency(amount: float, currency: str = 'CLP') -> str:
    """
    Formatea un monto según la moneda especificada
    """
    if currency == 'CLP':
        return f"${amount:,.0f} CLP"
    elif currency == 'UF':
        return f"{amount:.2f} UF"
    elif currency == 'USD':
        return f"${amount:.2f} USD"
    return str(amount) 
    