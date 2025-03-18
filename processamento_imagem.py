import cv2
import numpy as np

def processar_imagem(imagem):
    """
    Processa a imagem capturada para identificar padrões do gráfico.
    :param imagem: Imagem da tela em formato numpy array.
    :return: Imagem processada e contornos encontrados.
    """
    # Convertendo para tons de cinza
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicando detecção de bordas (Canny)
    edges = cv2.Canny(img_gray, 50, 150)

    # Encontrando contornos das velas
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return edges, contours

if __name__ == "__main__":
    from captura_tela import capturar_tela

    img = capturar_tela()
    edges, contornos = processar_imagem(img)

    cv2.imshow("Bordas Detectadas", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
