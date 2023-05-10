def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for t, k in queries:
        t -= 1
        while t > 0:
            if k <= len(S):
                if S[k - 1] == 'A':
                    S = 'BC' + S[k:]
                elif S[k - 1] == 'B':
                    S = 'CA' + S[k:]
                else:
                    S = 'AB' + S[k:]
                break
            else:
                t -= 1
                k -= len(S)
        print(S[k - 1])

if __name__ == '__main__':
    main()