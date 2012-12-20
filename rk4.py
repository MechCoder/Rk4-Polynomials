import math


def exp(u , x):
    '''Enter value of degree of f(x) and degree of x'''
    
    arrayx = range(x + 1)
    arrayu = range(u + 1)
    for i in range(x + 1):    
        arrayx[i] = input('Enter coefficient of %s power of x ' % str(i))
    for i in range(1 , u + 1):
        arrayu[i] = input('Enter coefficient of %s power of u ' % str(i))
    value = input('Enter the known value of x ')
    functionvalue = input('Enter the function value at that point ')
    answer = input('Enter the value at which you want to find the differential ')
    if answer > value:
        delta = 0.1
    else:
        delta = -0.1     
    stages = (answer - value) / delta
   
    deficit = answer - (value + (int(stages) * delta))
         
    if deficit == 0:
        stages = range(int(stages))
    else:
        stages = range(int(stages) + 1)
      
    for j in stages:
        if j == stages[-1] and deficit != 0.0:                 
            delta = deficit
               
        k1 = 0 ; k2 = 0 ; k3 = 0; k4 = 0
        for i in range(len(arrayx)):
            k1 = k1 + arrayx[i] * math.pow(value , i)
        for i in range(len(arrayu)):
            k1 = k1 + arrayu[i] * math.pow(functionvalue , i)
        value = value + (delta / 2)
        functionvalue = functionvalue + (k1 * delta / 2)
        for i in range(len(arrayx)):
            k2 = k2 + arrayx[i] * math.pow(value , i)
        for i in range(len(arrayu)):
            k2 = k2 + arrayu[i] * math.pow(functionvalue , i)
        functionvalue = functionvalue - (k1 * delta / 2) + (k2 * delta / 2)
        for i in range(len(arrayx)):
            k3 = k3 + arrayx[i] * math.pow(value , i)
        for i in range(len(arrayu)):
            k3 = k3 + arrayu[i] * math.pow(functionvalue , i)
        value = value + (delta / 2)
        functionvalue = functionvalue - (k2 * delta / 2) + (k3 * delta)
        for i in range(len(arrayx)):
            k4 = k4 + arrayx[i] * math.pow(value , i)
        for i in range(len(arrayu)):
            k4 = k4 + arrayu[i] * math.pow(functionvalue , i)
        functionvalue = functionvalue - (k3 * delta)
        
        answer = functionvalue + (((k1 + 2 * (k2 + k3) + k4) * delta) / 6)     
        functionvalue = answer
       
       
                      
    return answer                                         
         

