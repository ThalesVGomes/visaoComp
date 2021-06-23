# Transformar imagem em greyscale

import numpy as np
from skimage.color import rgb2gray
from skimage import io
import os


caminho_fotos = r'C:\Users\Thales\Desktop\Imagens Objetos' # Caminho das fotos ORIGINAIS


def add_suffix(base_name, suffix):  # Para transformar os nomes das imagens
    """Recebe o nome do arquivo com uma extensão e retorna o nome + sufixo + extensão
    Ex:
    base_name = 'foto123.jpg'
    suffix = '-nova'
    Retorna -> 'foto123-nova.jpg' """
    nome, ext = os.path.splitext(base_name)
    return nome + suffix + ext


def convert_greyscale(caminho_fotos): # Recebe as fotos ORIGINAIS
    save_path_base = r'C:\Users\Thales\Desktop\Greyscale'
    for root, dirs, fotos in os.walk(caminho_fotos):
        for foto in fotos:
            img_path = os.path.join(caminho_fotos, foto)  # Ajusta o caminho
            # Processamento da imagem
            img = io.imread(img_path)  # Lê a imagem (transforma em matriz)
            img = rgb2gray(img)  # Aplica um filtro de escala de cinza
            img = (img * 255).astype(np.uint8)  # Converte para números inteiros positivos até 255
            # Salvamento
            novo_nome = add_suffix(foto, '-cinza')
            save_path = os.path.join(save_path_base, novo_nome)
            io.imsave(save_path, img)  # Salva a imagem convertida


def log_image(caminho_fotos_cinzas): # Recebe as fotos CINZAS
    save_path_base = r'C:\Users\Thales\Desktop\Log'
    for root, dirs, fotos in os.walk(caminho_fotos_cinzas):
        for foto in fotos:
            img_path = os.path.join(caminho_fotos_cinzas, foto)  # Ajusta o caminho
            # Processamento da imagem
            img = io.imread(img_path)  # Lê a imagem (transforma em matriz)
            img = np.where(img == 0, 1, img)  # Transforma os 0 em 1 para ser possível calcular o log
            c = 255 / np.log(1 + np.max(img))
            log_img = c * np.log(img)
            log_img = log_img.astype(np.uint8)
            # Salvamento
            novo_nome = add_suffix(foto, '-log')
            save_path = os.path.join(save_path_base, novo_nome)
            io.imsave(save_path, log_img)  # Salva a imagem convertida


def exp_image(caminho_fotos_cinzas): # Recebe as fotos CINZAS
    save_path_base = r'C:\Users\Thales\Desktop\Exp'
    for root, dirs, fotos in os.walk(caminho_fotos_cinzas):
        for foto in fotos:
            img_path = os.path.join(caminho_fotos_cinzas, foto)  # Ajusta o caminho
            # Processamento da imagem
            img = io.imread(img_path)  # Lê a imagem (transforma em matriz)

            c = 0.0217  # Valor para y = 255 e x = 255
            exp_img = np.exp(c * img) - 1
            exp_img = exp_img.astype(np.uint8)
            # Salvamento
            novo_nome = add_suffix(foto, '-exp')
            save_path = os.path.join(save_path_base, novo_nome)
            io.imsave(save_path, exp_img)  # Salva a imagem convertida


from scipy.signal import convolve2d


def mean_filter(caminho_foto_cinza): # Recebe as fotos CINZAS
    """
    Para cada ponto (salvo as bordas) haverá 8 pontos vizinhos, conforme matriz:

    P1 P2 P3
    P4 Ponto P6
    P7 P8 P9

    Dessa forma, o filtro da média se baseará na média dos valores rgb de cada ponto
    Portanto, cada ponto da região terá peso de 1/9
    """

    save_path = r'C:\Users\Thales\Desktop\Mean'
    img = io.imread(caminho_foto_cinza)
    kernel = np.full(shape=(3, 3), fill_value=1 / 9)
    mean_filter_image = convolve2d(img, kernel, mode='same')  # 'same' garante que o tamanho da imagem seja mantido
    mean_filter_image = mean_filter_image.astype(np.uint8)
    io.imsave(save_path, mean_filter_image)
