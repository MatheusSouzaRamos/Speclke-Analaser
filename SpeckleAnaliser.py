import cv2 as cv
import numpy as np
import os
from math import sqrt

global c, save, el, q, img, h, w, I, graphic, s, imgtovideo_folder, caminho_salvar, imgs

class SA:
    def matrizdn(heigth, width):
        m = [0] * (heigth * width)
        return m

    def set_folder(caminho):
        global c, el, q
        c = caminho
        el = os.listdir(c)
        q = int(len(el) + 1)

    def Picture():
        global img, h, w, I, graphic

        img = cv.imread(c + '/imagem1.png')
        h, w, _ = img.shape
        imga = img
        del (img)

        I = SA.matrizdn(h, w)

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
          
    def colorPicture(RED, GREEN, BLUE):

        a1 = q // 2 + q // 3
        a2 = a1 // 2 + a1//4
        a3 = a2 // 2
        
        #p = (RED + GREEN + BLUE) / (q - 1)

        rr = RED / (q - 1)
        gg = GREEN / (q - 1)
        bb = BLUE / (q - 1)

        i = 0
        for y in range(0, h):
            for x in range(0, w):
                if I[i] >= a1:
                    r = I[i] * rr
                    g = 0
                    b = 0
                elif I[i] >= a2:
                    r = I[i] * rr
                    g = I[i]/2 * gg
                    b = 0
                elif I[i] >= a3:
                    r = 0
                    g = I[i] * gg
                    b = 0
                else:
                    r = 0
                    g = 0
                    b = 255 * bb
                graphic[y, x] = b, g, r
                i += 1

        print('concluido')

    def set_folder_save(caminho_salvar):
        global save
        save = f'{caminho_salvar}/'

    def savePicture():
        global s, save

        s = int(len(os.listdir(save)))

        name = f'{save}grafico{s+1}.png'

        cv.imwrite(name, graphic)

    def PictureForVideo(n):
        global img, h, w, I, graphic, average, average_2, imgs

        img = cv.imread(c + '/imagem1.png')
        h, w, _ = img.shape
        imga = img
        del (img)

        I = SA.matrizdn(h, w)

        graphic = np.zeros((h, w, 3), dtype='uint8')

        n = 0
        for u in range (1, average + 1):
            for i in range(1, average + 1):
                print(f'lendo imagem {n + i}')
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

            n = average_2
            average_2 += average

            print('n = {}'.format(n))
            print('average_2 = {}'.format(average_2))

            SA.colorPicture(255,127,63)
            imgs.append(graphic.copy())

            print('Feito uma parte')

    def video(caminho):
        global c, average, imgs, q, el, average_2
        imgs = []
        SA.set_folder(caminho)

        
        average = int(sqrt(len(el)))
        average_2 = average
        print(average)
        SA.PictureForVideo(average)

        name = 'videoSpeckle.avi'
        fps = 1
        height, width, layers = imgs[0].shape

        fourcc = cv.VideoWriter_fourcc(*'XVID')  # Codec de vídeo
        video = cv.VideoWriter(name, fourcc, fps, (width, height))

        for img in imgs:
            video.write(img)

        video.release()

    def SaveVideo(caminho):
        global imgs





SA.video('/home/suehtam/Documents/paint')