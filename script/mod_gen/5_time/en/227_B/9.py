def main():
    N = int(input())
    S = list(map(int, input().split()))
    #print(N)
    #print(S)
    a = 0
    b = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            a = S[i] - S[j]
            if a < 0:
                a = a * -1
            for k in range(N):
                if i == k or j == k:
                    continue
                b = S[i] - S[k]
                if b < 0:
                    b = b * -1
                if a + b == 0:
                    print('No')
                    return
    print('Yes')
    return

if __name__ == '__main__':
    main()