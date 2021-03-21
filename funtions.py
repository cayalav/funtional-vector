import numpy as np
from statistics import mode 

def random_arr(n): #Generador Array
  return np.random.randint(15, size=n) 

def multiply_list(arr): #Productoria
  result = 1
  for x in arr:
    result = result * x 
  return result 

def even_arr(arr): #Pares
  count=0
  for x in arr:
    if (arr[x]%2==0):
      count+=1
  return count 
  
def odd_arr(arr): #Impares con negación
  count=0
  for x in arr:
    if (not arr[x]%2==0):
      count+=1
  return count 

def prime_arr(num):
    count=0
    for n in num:
      if n>1:
         for i in range(2,n):
            if (n%i)==0:
                break
            else:
                count+=1
    return count

def sum_btw_arr(arr_one, arr_two): #Suma entre arrays
  result =np.add(arr_one, arr_two)
  return result

def rest_btw_arr(arr_one, arr_two): #Resta entre arrays
  result =np.subtract(arr_one, arr_two)
  return result

def most_frequent(arr_one): #Numero más repetido
    return(mode(arr_one)) 
    