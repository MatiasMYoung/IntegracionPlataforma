import requests
from typing import Dict

def get_currency_values() -> Dict[str, float]:
    """
    Obtiene los valores actuales de UF y USD desde mindicador.cl
    Returns:
        Dict con los valores de UF y USD
    """
    try:
        response = requests.get('https://mindicador.cl/api')
        data = response.json()
        
        return {
            'uf': float(data['uf']['valor']),
            'usd': float(data['dolar']['valor'])
        }
    except Exception as e:
        print(f"Error al obtener valores de monedas desde mindicador: {e}")
        return None 

if __name__ == '__main__':
    valores = get_currency_values()
    if valores:
        print("Valores obtenidos:")
        print(valores) 