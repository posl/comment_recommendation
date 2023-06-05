def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(H, W, N)
    # print(A)
    # print(B)
    # 要用set，否则会超时
    setA = set(A)
    setB = set(B)
    # print(setA)
    # print(setB)
    # 把set转换成list，否则会超时
    listA = list(setA)
    listB = list(setB)
    # print(listA)
    # print(listB)
    # listA.sort()
    # listB.sort()
    # print(listA)
    # print(listB)
    dictA = {}
    dictB = {}
    for i in range(len(listA)):
        dictA[listA[i]] = i + 1
    for i in range(len(listB)):
        dictB[listB[i]] = i + 1
    # print(dictA)
    # print(dictB)
    for i in range(N):
        print(dictA[A[i]], dictB[B[i]])

if __name__ == '__main__':
    main()