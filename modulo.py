#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

PI35DT = 3.1415926535897931159979634685441852
 
def calcular_pi (n): 
  sumatorio=0.0
  ini=0
  intervalos=1.0/float(n)
  for i in range(n):
    x_i=((i+1) - 1.0/2.0)/n
    fx_i=4.0/(1.0 + x_i*x_i)
    ini+=intervalos
    sumatorio+=fx_i
  valor_pi=sumatorio/n
  return (valor_pi)
  
  
#Programa principal


def error(n,aprox,umbral):
  intervalo = n
  lista =[]
  for i in range(aprox):
    valor = calcular_pi (intervalo)
    lista.append (valor)
    intervalo+=n
  diferencia = []
  for i in range (aprox):
    dif = abs (PI35DT - lista[i])
    diferencia.append (dif)
  correcto=0
  for i in range (aprox):
    if (diferencia[i]<=umbral):
      correcto=correcto + 1
  porcentaje=100.0*(1.0 - (float(correcto) / float(aprox)))
  return(porcentaje)
  
    
if (__name__=="__main__"):
  argumentos=sys.argv[1:]
  if(len(argumentos)==3):
    n=int(argumentos[0])
    aprox=int(argumentos[1])
    umbral=float(argumentos[2])
  else:
    print "Introduzca el número de intervalos (n>0): "
    n=int(raw_input())
    print "Introduzca el número de aproximaciones: "
    aprox=int(raw_input())
    print "Introduzca el umbral de error: "
    umbral=float(raw_input())
  if (n>0):
    porcentaje=error(n,aprox,umbral)
    print "El porcentaje de fallo es del ", porcentaje
 #   print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"  
  #for i in range (aprox):
   # print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista[i],diferencia[i])
  else:
    print "El valor de los intervalos debe ser positivo"

