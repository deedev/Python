def Max(A):
    max = A[0]
    for i in range(1,len(A),+1):
        if max < A[i]: max = A[i]
    return max
def Min(A):
    min = A[0]
    for i in range(1,len(A),+1):
        if min > A[i]: min = A[i]
    return min

def CountingSort(A):
    step = min(A)
    Result = [0]*len(A)
    sumCount = [0]*(1 + (max(A) - min(A)))
    for i in range(0,len(A),+1):
        sumCount[A[i]-step] += 1
    for i in range(1,len(sumCount),+1):
        sumCount[i] = sumCount[i-1] + sumCount[i]
    for i in range(len(A)):
        Result[sumCount[A[i]-step] - 1] = A[i]
        sumCount[A[i]-step] -= 1
    print (sumCount)
    return Result

A = [10,7,12,4,9,13,2,8,10,11,10]
print ("After:", CountingSort(A))
