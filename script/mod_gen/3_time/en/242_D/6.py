def main():
    #input
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        #compute
        if t%3 == 0:
            if k <= len(S):
                ans = S[k-1]
            else:
                k -= len(S)
                k %= 3
                if k == 0:
                    ans = S[-1]
                elif k == 1:
                    ans = S[-2]
                else:
                    ans = S[-3]
        elif t%3 == 1:
            if k <= len(S):
                ans = S[k-1]
            else:
                k -= len(S)
                k %= 3
                if k == 0:
                    ans = S[-1]
                elif k == 1:
                    ans = S[-3]
                else:
                    ans = S[-2]
        else:
            if k <= len(S):
                ans = S[k-1]
            else:
                k -= len(S)
                k %= 3
                if k == 0:
                    ans = S[-1]
                elif k == 1:
                    ans = S[-2]
                else:
                    ans = S[-3]
        #output
        print(ans)

if __name__ == '__main__':
    main()