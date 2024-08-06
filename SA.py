import cv2 as cv
import numpy as np
import os

def matrizdn(heigth, width):
    m = [0] * (heigth * width)
    return m

#caminho pasta de imgs ---altere---
c = '/home/suehtam/Documents/Speclke-Analaser/parafusoquente/parafusoquente'
#talvez necessario alterar a precisao de cores para o resultado a depender da qntd de imagens

#caminho para salvar ---altere---
save = '/home/suehtam/Documents/Speclke-Analaser/salvarimagens'

img = cv.imread(c + '/imagem1.png')
h, w, _ = img.shape
del (img)

I = matrizdn(h, w)

el = os.listdir(c)
q = len(el) + 1

a1 = q // 2 + q // 3 + 30
#a1 = q//2
a2 = a1 // 2 + a1//4
a3 = a2 // 2
p = 255 / (q - 1)

imga = cv.imread(c + '/imagem1.png')

graphic = np.zeros((h, w, 3), dtype='uint8')

for i in range(1, q):
    print(f'lendo imagem {i}')
    img = cv.imread(c + '/imagem{}.png'.format(i))

    print(imga[0, 0])
    print(img[0, 0])

    j = 0
    for y in range(0, h):
        for x in range(0, w):
            if not all(img[y, x] == imga[y, x]):
                I[j] += 1
            j += 1

    imga = img

i = 0
for y in range(0, h):
    for x in range(0, w):
        if I[i] >= a1:
            r = I[i] * p
            g = 0
            b = 0
        elif I[i] >= a2:
            r = I[i] * p
            g = I[i]/2 * p
            b = 0
        elif I[i] >= a3:
            r = 0
            g = I[i] * p
            b = 0
        else:
            r = 0
            g = 0
            b = 255 * p
        graphic[y, x] = b, g, r
        i += 1

s = len(os.listdir(save))
name = f'{save}grafico{s+1}.png'
cv.imwrite(name, graphic)

cv.imshow('graphic', graphic)
cv.waitKey(0)
cv.destroyAllWindows()

'''

#importação das bibliotecas necessárias para manipulação de imagem e buscas no computador
import cv2 as cv
import numpy as np
import os

#função que define uma matriz para armazenar valores de variação das imagens
def matrizdn(heigth, width):
    m = [0] * (heigth*width)
    return m

#caminho da pasta de imagens ----ALTERAR AQUI-----
c = 'C:/Users/strik/Desktop/testesimples'

#definindo altura e largura automaticamente com o caminho
img = cv.imread(c+'/imagem1.png')
h, w, _ = img.shape
del(img)

#usando a função matriz de acordo com o tamanho da imagem atual altura x largura
I = matrizdn(h, w)

#ajustando o tamanho do laço de acordo com o caminho da pasta de imagens
el = os.listdir(c)
q = len(el) + 1

#definindo a precisão de cores de acordo com a quantidade de imagens presentes na pasta
a1 = q//2 + q//4
a2 = a1//2
p = 255/(q-1)

#definindo a imagem1 como imagem anterior para a analise no laço
imga = cv.imread(c+'/imagem1.png')

#criando uma imagem limpa para transformar em grafico
grafic = np.zeros((h, w, 3), dtype='uint8')

#inicio do laço para a comparação de imagens passando por todas as imgs da pasta (qtd)
for i in range(1,q):
    print(f'lendo imagem {i}')
    img = cv.imread(c+'/imagem{}.png'.format(i))

    print(imga[0,0])
    print(img[0,0])

    #inicio do laço para a comparação de todos os pixels das imagens em y e x
    j = 0
    for y in range(0,h):
        for x in range(0,w):
            if not all(img[y,x] == imga[y,x]):
                I[j] += 1
            j += 1
    #atribuição da imagem atual para a imagem anterior, assim a proxima será analisada com base nesta
    imga = img

#inicio do laço de processamento do grafico, ajustando o valor de intensidade com as cores rgb
i = 0
for y in range(0, h):
    for x in range(0, w):
        if I[i] >= a1:
            r = I[i] * p
            g = 0
            b = 0
        elif I[i] > a2:
            r = 0
            g = I[i] * p
            b = 0
        else:
            r = 0
            g = 0
            b = 255 #*p
        grafic[y,x] = b, g, r
        i += 1

#exibição do grafico formado
cv.imshow('grafic', grafic)
cv.waitKey(0)
cv.destroyAllWindows()

'''

