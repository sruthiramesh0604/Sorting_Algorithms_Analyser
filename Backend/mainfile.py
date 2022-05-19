#Name: FNU Sruthi Ramesh
#UTA ID: 1001964707

import numpy as np
import time
import eel
import sortingalgos as prog


print("Choose:")
print("1. Enter the numbers")
print("2. Generate random numbers")
choice=int(input())

#This function generates random integers and stores it into an array which we later on pass to the algorithms
def generateNum(value):
    iptarr=np.random.randint(0,1000,val).tolist()
    print(iptarr)
    return iptarr

# Checking with the user if the user wants to enter numbers manually or generate random integers
if choice==1:
    print("Enter the size of the data set you want to sort!")
    size=int(input())
    arr=[]
    for i in range(size):
        print("enter the number:")
        value=int(input())
        arr.append(value)
    print(arr)


elif choice==2:
    print("Enter the size of the data set you want to sort!")
    val=int(input())
    arr = generateNum(val)
    


print("choose from the below list of algorithms:")   
print("1.Merge Sort  2.Heap Sort  3.Quick sort(Regular)  4.Quick sort using 3 median  5.Insertion  6.Selection  7.Bubble sort") 
#Asking the user to choose the algorithm using wheich we will sort the numbers
chc=int(input())
if chc==1:
    start=time.time()# Using the time function to record the execution time
    prog.mergeSort(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==2:
    start=time.time()
    prog.heapSort(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==3:
    start=time.time()
    prog.regularQuickSort(arr,0,len(arr)-1)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==4:
    start=time.time()
    prog.quicksortByMedian(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==5:
    start=time.time()
    prog.insertionSort(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==6:
    start=time.time()
    prog.selectionSort(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)

if chc==7:
    start=time.time()
    prog.bubbleSort(arr)
    end=time.time()
    print(arr)
    total=end-start
    print(total)



