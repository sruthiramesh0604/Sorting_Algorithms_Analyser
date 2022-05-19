#Name: FNU Sruthi Ramesh
#UTA ID: 1001964707
#References:
# https://stackoverflow.com/questions/24533359/implementing-the-quick-sort-with-median-of-three
# https://www.google.com/search?q=quick+sort+using+3+medians&rlz=1C1CHBF_enIN950IN950&oq=quick+sort+using+3+medians&aqs=chrome..69i57j33i22i29i30l2.722j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_Nh9bYoy0Iu3dqtsPlsirgAw17


import numpy as np
import time

# This function implements Merge sort where we take an array and divide the array into sub arrays
# till each sub array has only one element each
def mergeSort(inputarr):

    if len(inputarr)>1: #Checking if the array size is greater than 1
        #Divide the array into 2 arrays(left sub array and right sub array)
        left_arr=inputarr[:len(inputarr)//2] 
        right_arr=inputarr[len(inputarr)//2:]

#recursive function to divide the arrays till each sub array has only 1 element
        mergeSort(left_arr)
        mergeSort(right_arr)

        i=0
        j=0
        k=0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                inputarr[k]=left_arr[i]
                i+=1

            else:
                inputarr[k]=right_arr[j]
                j+=1
            k+=1

        while i<len(left_arr):
            inputarr[k]=left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):
            inputarr[k]=right_arr[j]
            j+=1
            k+=1
    return inputarr

# mergeSort(iptarr)
# print(iptarr)

#This function implements Heapsort. Here we have implemented max heap, where the parent node is always
#greater than the child node and the largest node is selected as the root node.

def swap(lst,i,j):
    lst[i],lst[j]=lst[j],lst[i]

#This is the implementation of heapify function where the last leaf node is swappped with the root node
def siftDown(lst,i,upper):
    while (True):
        l,r=i*2+1,i*2+2
        if max(l,r)<upper:
            if lst[i] >=max(lst[l],lst[r]): break
            elif lst[l]>lst[r]:
                swap(lst,i,l)
                i=l
            else:
                swap(lst,i,r)
                i=r
        elif l<upper:
            if lst[l]>lst[i]:
                swap(lst,i,l)
                i=l
            else: break
        elif r<upper:
            if lst[r]>lst[i]:
                swap(lst,i,r)
                i=r
            else: break
        else: break

def heapSort(lst):
    for j in range((len(lst)-2)//2,-1,-1):
        siftDown(lst,j,len(lst))
    
    for end in range (len(lst)-1,0,-1):
        swap(lst,0,end)
        siftDown(lst,0,end)

    return lst

# heapSort(iptarr)
# print(iptarr)


#This is the regular quick sort where the last element is selected as the pivot element
def regularQuickSort(arr, left, right):
    if left<right:
        partition_pos= partition(arr,left,right)
        regularQuickSort(arr,left,partition_pos -1)
        regularQuickSort(arr,partition_pos+1,right)
#We are considering 2 pointers where i points to the left most element and j points to the last but one element
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]

    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
    return arr

#This function implements Quick sort using 3 median 
def quicksortByMedian(arr):
    quicksorta(arr, 0, len(arr) - 1)
    return arr


def quicksorta(arr, l, r):
    if r - l + 1 <= 3:
        quicksortb(arr, l, r)
    else:
        median = medianofthree(arr, l, r)
        parting_of_array = dividesort(arr, l, r, median)
        quicksorta(arr, l, parting_of_array - 1)
        quicksorta(arr, parting_of_array + 1, r)


def medianofthree(arr, l, r):
    m = (l + r) / 2
    if arr[int(l)] > arr[int(m)]:
        swapsort(arr, l, m)
    if arr[int(l)] > arr[int(r)]:
        swapsort(arr, l, r)
    if arr[int(m)] > arr[int(r)]:
        swapsort(arr, m, r)
    swapsort(arr, m, r - 1)
    return arr[int(r - 1)]


def swapsort(arr, a, b):
    arr[int(a)], arr[int(b)] = arr[int(b)], arr[int(a)]


def dividesort(arr, l, r, divide_pivot):
    l1 = l
    r1 = r - 1
    while True:
        l1 += 1
        while arr[int(l1)] < divide_pivot:
            l1 += 1
        r1 -= 1
        while arr[int(r1)] > divide_pivot:
            r1 -= 1
        if l1 >= r1:
            break
        else:
            swapsort(arr, l1, r1)
    swapsort(arr, l1, r - 1)
    return l1


def quicksortb(arr, l, r):
    if r - l + 1 <= 1:
        return
    if r - l + 1 == 2:
        if arr[int(l)] > arr[int(r)]:
            swapsort(arr, l, r)
        return
    else:
        if arr[int(l)] > arr[int(r - 1)]:
            swapsort(arr, l, r - 1)
        if arr[int(l)] > arr[int(r)]:
            swapsort(arr, l, r)
        if arr[int(r - 1)] > arr[int(r)]:
            swapsort(arr, r - 1, r)


# quickSort(iptarr)
# print(iptarr)

# This function implements the Insertion sort where it sorts the array in place by comparing it 
# with the other elements of the array

#Worst Case Time Complexity ==> O(n**2)
#Best Case Time Complexity ==> O(n)

def insertionSort(array):

    for i in range(len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = element
    return array

# insertionSort(iptarr)
# print(iptarr)
 
##This function implements the selection sort which swaps elements by comparing the value
#Worst Case Time Complexity ==> O(n*2)
#Best Case Time Complexity ==> O(n)

def selectionSort(array):

    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[min], array[i] = array[i], array[min]

    return array
# selectionSort(iptarr)
# print(iptarr)

#Sorts the array using divide and merge algorithm which picks one element 
# as a pivot and then sorts the array according to the value of the pivot
#Worst Case Time Complexity ==> O(n**2) 
#Best Case Time Complexity ==> O(nlog(n))

def bubbleSort(array):

    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

# bubbleSort(iptarr)
# print(iptarr)



