def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N):
        tmp = 0
        tmpC = []
        j = i
        while True:
            tmp += C[P[j] - 1]
            tmpC.append(C[P[j] - 1])
            j = P[j] - 1
            if j == i:
                break
        if tmp > 0:
            num = K // len(tmpC)
            ans = max(ans, tmp * num + sum(tmpC[:K % len(tmpC)]))
        else:
            ans = max(ans, sum(tmpC[:K]))
    print(ans)

if __name__ == '__main__':
    main()