def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = sorted(list(map(int, input().split())))
    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)
    if len(A) == 2:
        print(1)
        return
    # print(A)
    diff = []
    for i in range(1, len(A)):
        diff.append(A[i]-A[i-1]-1)
    # print(diff)
    k = min(diff)
    res = 0
    for i in range(len(diff)):
        res += diff[i]//k
        if diff[i]%k != 0:
            res += 1
    print(res)

if __name__ == '__main__':
    main()