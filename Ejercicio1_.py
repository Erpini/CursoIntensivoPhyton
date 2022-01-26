
import os
import humanize

ruta = "C:/Users/Pini/Downloads"
archivos = os.listdir(ruta)


for archivoActual in archivos:
   completa = os.path.join(ruta, archivoActual)
   tamañoArchivos = os.path.getsize(completa)
   tamañoReal = humanize.naturalsize(tamañoArchivos)



   if os.path.isfile(completa):
        print(archivoActual, 'Esto es un archivo y pesa', tamañoReal)

   else:
       print(archivoActual, "no es un archivo")


for ruta, dir. file in os.walk(ruta):
    for name in file:
        print(os.path.join(root, name))
    for name in dir:
        print(os.path.join(root, name))