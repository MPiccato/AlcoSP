from io import open

archivo_texto = open('C:\Users\Talia\Documents\cargaalquista\build\ar.txt', "w")

frase = '2019-11-26'

archivo_texto.write(frase)


archivo_texto.close()