def Partition(A, L, H):
    pivot = A[H]
    index = L
    current = L
    while(current < H):
        if(A[current] <= pivot):
            A[index], A[current] = A[current], A[index]
            index += 1
        current += 1
    A[index], A[H] = A[H], A[index]
    return index

def QuickSort(A, start, end):
    if(start < end):
        index = Partition(A, start, end)
        QuickSort(A, start, index - 1)
        QuickSort(A, index + 1, end)

A = [2,5,11,9,6,1]
QuickSort(A,0,len(A) - 1)
print (A)
