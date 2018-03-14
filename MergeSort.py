def Merge(L,R):
    Result = []
    i,j = 0,0
    while i < len(L) and j < len(R):
        if (L[i] < R[j]):
            Result.append(L[i])
            i += 1
        else:
            Result.append(R[j])
            j += 1
    Result += L[i:]
    Result += R[j:]
    return Result

def MergeSort(A):
    if (len(A) <= 1):
        return A
    Mid = int(len(A)/2)
    L = MergeSort(A[:Mid])
    R = MergeSort(A[Mid:])
    return Merge(L,R)

A = [16, 9, 3]
print (MergeSort(A))
