#!/usr/bin/python
#!encoding: UTF-8
import sys
import modulo
import time
import timeit
  
  
#Programa principal
  
argumentos=sys.argv[1:]
if(len(argumentos)==8):
	n=int(argumentos[0])
	aprox=int(argumentos[1])
	umbral=[]
	for i in range (2,7):
		umbral.append(float(argumentos[i]))
	nombre_fich=argumentos[7]
else:
	print "Introduzca el número de intervalos (n>0): "
	n=int(raw_input())
	print "Introduzca el número de aproximaciones: "
	aprox=int(raw_input())
	print "Introduzca 5 umbrales de error: "
	umbral=[]
	for i in range (5):
		print "Introduzca el umbral",i, ":"
		umbral.append(float(raw_input()))
	print "Introduzca el nombre del fichero para almacenar los resultados: "
	nombre_fich=raw_input()
if (n>0):
	try:
		fichero=open(nombre_fich, "a")
	except:
		fichero=open(nombre_fich, "w")
	fichero.write("Nº de intervalos: %d\n" % (aprox))
	for i in range(5):
		start=time.time()
		modulo.error(n,aprox,umbral[i])
		finish=time.time()-start
		t1=timeit.Timer("modulo.error(n,aprox,umbral)","from__main__import modulo; n=%d;aprox=%d; umbral=%f" % (n,aprox,umbral[i]))
		print t1.timeit(10)
		fichero.write("%2.10f\n" % (finish)) 
	fichero.close()
else:
	print "El valor de los intervalos debe ser mayor que 0"
  

  
  
  
 
