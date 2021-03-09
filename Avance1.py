import cv2
#############################################
# Accedemos a la webcam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
# leemos el xml
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,0)
count = 0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # obtenemos la imagen de la webcam
    numeroPlaca = nPlateCascade.detectMultiScale(imgGray, 1.1, 10) # detectamos la posible placa
    for (x, y, w, h) in numeroPlaca:
        area = w*h
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Numero de Placa",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w] # definimos la region de la placa
            cv2.imshow("Numero de Placa", imgRoi) # obtenemos la imagen

    cv2.imshow("Resultado", img)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('s'):

        cv2.imwrite("Placas_Guardadas/Numero_Placa"+str(count)+".jpg",imgRoi)# Guardar
        # la imagen de interes
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Escaneo correcto",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2,(0,0,255),2) # mensaje de exito
        cv2.imshow("Resultado",img)
        cv2.waitKey(500) # delay para visualizar la confirmacion
        count +=1
    elif k == ord('q'):
        break
