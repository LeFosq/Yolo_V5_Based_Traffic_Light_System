import cv2
import os
diretorio = 'C:/Users/LuizF/PycharmProjects/YoloV5_Traffic_Light/semaforo/images' #Diretorio da imagem da "screenshot"
camera = cv2.VideoCapture(0) #Entidade câmera
return_value, image = camera.read() #Tira a "screenshot"
cv2.imwrite(os.path.join(diretorio,'x.jpg'), image) #Salva imagem obtida
del(camera)