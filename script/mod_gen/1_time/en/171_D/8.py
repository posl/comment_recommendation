def main():
    #read
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    
    #solve
    ans = [0] * Q
    dic = {}
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    total = sum(A)
    for i in range(Q):
        if B[i] in dic:
            total += (C[i] - B[i]) * dic[B[i]]
            if C[i] in dic:
                dic[C[i]] += dic[B[i]]
            else:
                dic[C[i]] = dic[B[i]]
            del dic[B[i]]
        ans[i] = total
    
    #print
    for i in range(Q):
        print(ans[i])

if __name__ == '__main__':
    main()