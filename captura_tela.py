import cv2
import numpy as np
import pyautogui

def capturar_tela(regiao=(0, 0, 1920, 1080)):
    """
    Captura a tela na região especificada.
    :param regiao: Tupla (x, y, largura, altura) para definir a área de captura.
    :return: Imagem capturada em formato numpy array.
    """
    screenshot = pyautogui.screenshot(region=regiao)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame

if __name__ == "__main__":
    img = capturar_tela()
    cv2.imshow("Captura de Tela", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
