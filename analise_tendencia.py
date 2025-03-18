import numpy as np
import cv2

def detectar_tendencia(contornos):
    """
    Analisa os contornos detectados para identificar tendências de alta ou baixa.
    :param contornos: Lista de contornos das velas.
    :return: String indicando tendência.
    """
    alturas = [cv2.boundingRect(cnt)[3] for cnt in contornos]

    if len(alturas) < 5:
        return "Dados insuficientes"

    media_alturas = np.mean(alturas[-5:])

    if alturas[-1] > media_alturas * 1.1:
        return "Tendência de Alta - Possível Compra 📈"
    elif alturas[-1] < media_alturas * 0.9:
        return "Tendência de Baixa - Possível Venda 📉"
    else:
        return "Mercado Lateralizado - Sem entrada"

if __name__ == "__main__":
    from captura_tela import capturar_tela
    from processamento_imagem import processar_imagem
    import cv2

    img = capturar_tela()
    _, contornos = processar_imagem(img)
    resultado = detectar_tendencia(contornos)

    print(resultado)
