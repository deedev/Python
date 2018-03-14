def Heapify(A,n,i):
    Largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and A[l] > A[Largest] :
        Largest = l
    if r < n and A[r] > A[Largest] :
        Largest = r
    if(Largest != i):
        A[i], A[Largest] = A[Largest], A[i]
        Heapify(A,n,Largest)

def HeapSort(A):
    n = len(A)
    index = int(n/2) - 1
    for i in range(index,-1,-1):
        Heapify(A,n,i)
    
    for i in range(n-1,0,-1):
        A[i],A[0] = A[0], A[i]
        print (A)
        Heapify(A,i,0)
  
A = [2,5,11,9,6,1]
HeapSort(A)
