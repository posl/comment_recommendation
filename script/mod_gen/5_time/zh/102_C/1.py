def find_min_sadness(N,A):
    #先找到中位数
    A.sort()
    if N%2==0:
        b = int((A[int(N/2)-1]+A[int(N/2)])/2)
    else:
        b = A[int(N/2)]
    #然后计算悲伤程度
    sadness = 0
    for i in range(N):
        sadness += abs(A[i]-(b+i+1))
    return sadness

if __name__ == '__main__':
    find_min_sadness()