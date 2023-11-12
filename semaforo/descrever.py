import cv2
import torch
import os
os.system('PegarImagem.py') #Executa o script de screenshot
file_path = "../semaforo/texto/arquivo.txt" #Diretório do arquivo .txt que conterá as informações inferidas
file = open(file_path, 'w')
model = torch.hub.load('ultralytics/yolov5' , 'yolov5s') #Escolhe o "treinamento" que será utilizado

im = cv2.imread('images/x.jpg')[..., ::-1]
im2 = cv2.imread('images/1.jpg')[..., ::-1]
results = model([im,im2],size=640) #Comando que realiza a identificação dos elementos, acionando o yolo.
content = str(results) #Transforma os resultados obtidos em um string que vai ser passado para o .txt
file.write(content)
file.close()
