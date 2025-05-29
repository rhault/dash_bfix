import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def fetch_omie(url: str, call: str, param: list) -> dict | None:
    OMIE_API_KEY = os.getenv("OMIE_KEY")
    OMIE_API_SECRET = os.getenv("OMIE_SECRET")
    OMIE_API_URL = os.getenv("OMIE_URL")

    headers = {"Content-type": "application/json"}

    payload = {
        "call": call,
        "param": param,
        "app_key": OMIE_API_KEY,
        "app_secret": OMIE_API_SECRET,
    }

    try:
        if OMIE_API_URL is None:
            raise ValueError("OMIE_API_URL environment variable is not set.")

        response = requests.post(
            f"{OMIE_API_URL}/{url}", headers=headers, data=json.dumps(payload)
        )
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        print(f"Conteúdo da resposta: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Erro de Conexão: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Erro de Timeout: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro na Requisição: {req_err}")
    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON.")
        print(f"Conteúdo da resposta: {response.text}")
    except ValueError as ve:
        print(f"Erro de Configuração: {ve}")

    return None
