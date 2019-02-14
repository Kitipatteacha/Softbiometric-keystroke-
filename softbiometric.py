import readchar
import time
import math
keep = {}
dict_index = ''

def keepData(index,time):
    if(dict_index not in keep):
        keep[index]= time
    else:
        keep[index]=(keep[index]+time)/2
        
def inputData():
    reset = True
    while 1:
        first = readchar.readchar()
        if(str(first)=="b'.'"):
            return
        start = time.time()
        if(reset==False):
            timeTaken2 = start-final
            print(str(second)+"-"+str(first)+": "+str(timeTaken2))
            dict_index2 = str(second)+str(first)
            keepData(dict_index2,timeTaken2)
            
        second = readchar.readchar()
        if(str(second)=="b'.'"):
            return
        final = time.time()
        timeTaken= final-start
        
        print(str(first)+"-"+str(second)+": "+str(timeTaken))
        dict_index = str(first)+str(second)
        keepData(dict_index,timeTaken)
        reset = False

def checkHowClose():
    allPercentError = []

    reset = True
    while 1:
        first = readchar.readchar()
        if(str(first)=="b'.'"):
            return sum(allPercentError)/len(allPercentError)
        start = time.time()
        if(reset==False):
            timeTaken2 = start-final
            print(str(second)+"-"+str(first)+": "+str(timeTaken2))
            dict_index2 = str(second)+str(first)
            if(dict_index2 in keep):
                allPercentError += [abs(keep[dict_index2]-timeTaken2)/keep[dict_index2]]
                
        second = readchar.readchar()
        if(str(second)=="b'.'"):
            return sum(allPercentError)/len(allPercentError)
        final = time.time()
        timeTaken= final-start
        
        print(str(first)+"-"+str(second)+": "+str(timeTaken))
        dict_index = str(first)+str(second)
        if(dict_index in keep):
                allPercentError += [abs(keep[dict_index]-timeTaken)/keep[dict_index]]
                
        reset = False
    

#Main

name = input("Enter your name: ")
print("press . to stop")
inputData()
print("press . to end identify process")
error = checkHowClose()
print("%Error: "+str(error))




