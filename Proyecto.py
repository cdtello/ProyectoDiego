from tkinter import *
from tkinter.filedialog import askopenfilename



def ejecutar(a):
    lyl = []  # la lista lyl es la que tiene longitud y latitud
    hhh = []  # la lista hhh es la que contiene las 3 alturas



    archivo=open(a,'r')
    lineas=list(archivo.read().splitlines())
    lineas.pop(0)




    for i in (lineas):
        linea=i.split(';')
        lyl.append([float(linea[0]),float(linea[1])])
        hhh.append([float(linea[2]),float(linea[3]),float(linea[4])])
    #print(hhh)
    #print("los datos de longitud y latitud del GPS son:",lyl)
    #print("Los datos de las alturas son:",hhh)


    a=[]
    b=[]
    d=[]

    for i in (hhh):
        a.append(i[0])
        b.append(i[1])
        d.append(i[2])



    c=d[0:(len(d)-1)]




    a1=a[0:(len(a)-1)]
    b1=b[0:(len(b)-1)]


    anterior=len(a)-1


    difelip=[]
    difgeo=[]
    difalt=[]


    #DETERMINACIÓN ENTRE LAS ALTURAS ELIPSOIDALES DEL PUNTO DE CALCULO Y LAS ESTACIONES DE ALTURA CONOCIDA#
    for elemento in a1:
        lista=a[len(a)-1]-elemento
        difelip.append(float(lista))


    ##DETERMINACIÓN DE LAS DIFERENCIAS DE ALTURA GEOIDALES ENTRE EL PUNTO DE CALCULOS Y LAS ESTACIONES DE ALTURA CONOCIDAS##
    for i in b1:
        lista2=b[len(b)-1]-i
        difgeo.append(float(lista2))


    ##DETERMINACIÓN DE LAS DIFERENCIAS DE ALTURA OTOMÉTRICAS GPS ENTRE EL PUNTO DE CALCULO Y LAS ESTACIONES DE ALTURA CONOCIDA##
    import numpy as np

    matriz1=np.matrix(difgeo)
    matriz2=np.matrix(difelip)


    alturasorto= matriz2-matriz1

    h=np.matrix(c)






    if len(c)==5:
        Hnivelca=float(c[2]-c[0])
        Hniveled=float(c[4]-c[3])
        Hnivelba=float(c[1]-c[0])
        Hnivelcd=float(c[2]-c[3])

        matrizvalores=np.matrix([[1,0,-1,0,0],[0,-1,0,0,1],[1,0,0,-1,0],[0,0,-1,0,1]])
        inversava=matrizvalores.I

        matrizpesos=np.matrix([[1,0,-1,0,0],[0,-1,0,0,1],[1,0,0,-1,0],[0,0,-1,0,1]])

        matriztransp=matrizvalores.T

        inversatransp=matriztransp.I

        matrizresul=np.matrix('%s;%s;%s;%s'%(Hnivelca,Hniveled,Hnivelba,Hnivelcd))

        matrizxeca=np.matrix('%s;%s;%s;%s;%s'%(alturasorto[0,0],alturasorto[0,1],alturasorto[0,2],alturasorto[0,3],alturasorto[0,4]))

        inversa= matrizpesos.I

        ##V=P^-1*Bt*(B*p^-1*Bt)^-1*(C-BL)##

        ##DONDE:
        #p=matrizvalores
        #b=matrizpesos
        #c=matrizresul
        y=(matrizvalores*matrizxeca)

        k=matrizresul-(matrizvalores*matrizxeca)

        j=(matriztransp*(((matriztransp*matrizvalores)*inversa).I))*inversa

        v=j*k

        L=matrizxeca+v


        matrixnivelada=np.matrix('%s;%s;%s;%s;%s'%(h[0,0],h[0,4],h[0,2],h[0,1],h[0,3]))


        print("altura nivelada del punto desconocido es:")
        print(matrixnivelada+L)

    if len(c)==4:
        Hnivelab=c[1]-c[0]
        Hnivelbc=c[2]-c[1]
        Hnivelcd=c[3]-c[2]


        matrizvalores=np.matrix([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]])

        inversava=matrizvalores.I
        matrizpesos=np.matrix([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]])
        matriztransp=matrizvalores.T
        inversatransp=matriztransp.I
        matrizresul=np.matrix('%s;%s;%s'%(Hnivelab,Hnivelbc,Hnivelcd))

        alturasorto2=np.matrix('%s;%s;%s;%s'%(alturasorto[0,0],alturasorto[0,1],alturasorto[0,2],alturasorto[0,3]))

        inversa=matrizpesos.I


        y=(matrizvalores*alturasorto2)

        k=matrizresul-(matrizvalores*alturasorto2)

        j=(matriztransp*(((matriztransp*matrizvalores)*inversa).I))*inversa

        v=j*k

        L=alturasorto2+v


        matrixnivelada=np.matrix('%s;%s;%s;%s'%(h[0,0],h[0,1],h[0,2],h[0,3]))

        print("altura nivelada del punto desconocido es:")
        print(matrixnivelada+L)
    if len(c)==3:

        Hnivelab=c[1]-c[0]
        Hnivelbc=c[2]-c[1]
        matrizvalores=np.matrix([[1,-1,0],[0,1,-1]])

        inversava=matrizvalores.I
        matrizpesos=np.matrix([[1,-1,0],[0,1,-1]])
        matriztranp=matrizvalores.T
        inversatransp=matriztranp.I
        matrizresul=np.matrix('%s;%s',(Hnivelab,Hnivelbc))
        alturasorto2=np.matrix('%s;%s;%s'(alturasorto[0,0],alturasorto[0,1],alturasorto[0,2]))
        inversa=matrizpesos.I

        y=(matrizvalores*alturasorto2)

        k=matrizresul-(matrizvalores*alturasorto2)

        j=(matriztransp*(((matriztransp*matrizvalores)*inversa).I))*inversa

        v=j*k

        L=alturasorto2+v


        matrixnivelada=np.matrix('%s;%s;%s;%s'%(h[0,0],h[0,1],h[0,2],h[0,3]))


        print("altura nivelada del punto desconocido es:")
        print(matrixnivelada+L)

    return matrixnivelada+L

    #if len(c)==2:
    #Creacion de Ventana


def BtnBuscarArchivoPresinado():
    print("Hola Mundo")
    abrirArchivo()

def BtnEjecutarPresionado():
    matrix = ejecutar(varRuta.get())
    cadena = "Altura Nivelada Del Punto Desconocido es: "+ str(matrix[0])
    varTexto.set(cadena)

    
def BtnManualPresionado():
    cadena = "MANUAL DE USO\n\n"
    cadena = cadena + "Paso1 : Presione Boton Abrir y Seleccion el Archivo .TXT\n"
    cadena = cadena + "Paso2 : Una vez Ruta Direccionada Presionar Boton Nivelar\n\n"
    cadena = cadena + "OBSERVACIONES : \n\n"
    cadena = cadena + "1: El Programa Ejecuta Max 5 datos Conocidos\n"
    cadena = cadena + "2: Formato Archivo Entrada : .txt\n"
    cadena = cadena + "3: El Archivo Maneja Una Estructura Especifica\n"
    cadena = cadena + "4: Dato 0 = Dato Desconocido\n\n"


    
    cadena = cadena + "ESTRUCTURA ARCHIVO .TXT\n\n"
    linea1="l;l;altuelip;alturageocol;alturanivelada\n"
    linea2="1;1;2610.8160;21.5668;2588.5523\n"
    linea3="1;1;2697.2876;20.9002;2673.2700\n"
    linea4="1;1;2580.7914;20.8347;2557.3867\n"
    linea5="1;1;2575.7611;20.9812;2552.5900\n"
    linea6="1;1;2577.5087;20.9799;2553.9538\n"
    linea7="1;1;3217.8420;21.5469;0"
    ejemploArchivo = linea1+linea2+linea3+linea4+linea5+linea6+linea7

    cadena = cadena + ejemploArchivo
    varTexto.set(cadena)


    
def abrirArchivo():
    name = askopenfilename(initialdir="",
                            filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                            title="Elija un archivo"
                            )
    varRuta.set(name)


ventana=Tk()
ventana.title("Conversion Alturas GPS-SNMM")
ventana.geometry("360x450")
ventana.resizable(width=False,height=False)



#***************************************************************************
#*********************Creacion de Elementos Iniciales***********************
#***************************************************************************
#Variable que recibe los datos

varRuta = StringVar()
varTexto = StringVar()
#Creacion del Entry
text = Label(ventana, height=23, width=47,bg="#FFFFFF",textvariable = varTexto).place(x = 10, y = 60)
label = Label(ventana,text="Ruta: ").place(x = 10, y = 10)
Eruta = Entry(ventana,width = 55,textvariable = varRuta).place(x = 10, y = 30)
#Creacion Boton
btnBuscarArchivo = Button(ventana, height = 1,width = 7,text="Abrir",command=BtnBuscarArchivoPresinado).place(x = 20, y = 420)
btnEjecutar = Button(ventana, height = 1,width = 7,text="Nivelar",command=BtnEjecutarPresionado).place(x = 135, y = 420)
btnManual = Button(ventana, height = 1,width = 7,text="Manual",command=BtnManualPresionado).place(x = 250, y = 420)

ventana.mainloop()
