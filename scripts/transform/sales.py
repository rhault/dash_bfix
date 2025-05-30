from ..extract import fetch_sales_data
from datetime import datetime


def new_sales_data(update_at: datetime) -> list[dict | None]:
    """
    This function processes the sales data and returns it in a new format.
    """
    sales_data = fetch_sales_data()
    new_format_data = []

    if not sales_data:
        return new_format_data

    for record in sales_data['pedido_venda_produto']:
        cabecalho = record.get("cabecalho", {})
        infoCadastro = record.get("infoCadastro", {})
        informacoes_adicionais = record.get("informacoes_adicionais", {})
        frete = record.get("frete", 0.0)
        total_pedido = record.get("total_pedido", 0.0)

        new_record = {
            'numero_pedido': cabecalho['numero_pedido'],
            'bloqueado': cabecalho['bloqueado'],
            'codigo_cenario_impostos': cabecalho['codigo_cenario_impostos'],
            'codigo_cliente': cabecalho['codigo_cliente'],
            'codigo_pedido': cabecalho['codigo_pedido'],
            'data_previsao': cabecalho['data_previsao'],
            'etapa': cabecalho['etapa'],
            'qtde_parcelas': cabecalho['qtde_parcelas'],
            'quantidade_itens': cabecalho['quantidade_itens'],
            'valor_frete': frete['valor_frete'],
            'autorizado': infoCadastro['autorizado'],
            'cancelado': infoCadastro['cancelado'],
            'dAlt': infoCadastro['dAlt'],
            # dFat may not always be present
            'dFat': infoCadastro.get('dFat', None),
            'dInc': infoCadastro['dInc'],
            'denegado': infoCadastro['denegado'],
            'devolvido': infoCadastro['devolvido'],
            'devolvido_parcial': infoCadastro['devolvido_parcial'],
            'faturado': infoCadastro['faturado'],
            'hAlt': infoCadastro['hAlt'],
            # hFat may not always be present
            'hFat': infoCadastro.get('hFat', None),
            'hInc': infoCadastro['hInc'],
            'codProj': informacoes_adicionais['codProj'],
            'codVend': informacoes_adicionais['codVend'],
            'codigo_categoria': informacoes_adicionais['codigo_categoria'],
            'codigo_conta_corrente': informacoes_adicionais['codigo_conta_corrente'],
            'consumidor_final': informacoes_adicionais['consumidor_final'],
            'base_calculo_icms': total_pedido['base_calculo_icms'],
            'valor_descontos': total_pedido['valor_descontos'],
            'valor_mercadorias': total_pedido['valor_mercadorias'],
            'valor_total_pedido': total_pedido['valor_total_pedido'],
            'updated_at': update_at.strftime("%d/%m/%Y %H:%M:%S")
        }
        new_format_data.append(new_record)
    return new_format_data
