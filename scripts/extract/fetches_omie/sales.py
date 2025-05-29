from ..fetch_api_omie import fetch_omie


def fetch_sales_data() -> dict | None:
    """Fetches sales the API"""
    url = "produtos/pedido/"
    call = "ListarPedidos"
    param_list = [
        {
            "pagina": 1,
            "registros_por_pagina": 100,
            "apenas_importado_api": "N",
            "numero_pedido_de": 9349,
            "numero_pedido_ate": 9349,
        }
    ]

    try:
        response = fetch_omie(url, call, param_list)
        return response
    except Exception as error:
        print(f"Error fetching data sales from API {error}")
        return None
