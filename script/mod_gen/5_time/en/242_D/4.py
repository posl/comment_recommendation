def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        for j in range(t):
            if S[k] == 'A':
                S = S[:k] + 'BC' + S[k+1:]
            elif S[k] == 'B':
                S = S[:k] + 'CA' + S[k+1:]
            elif S[k] == 'C':
                S = S[:k] + 'AB' + S[k+1:]
            k = (k + 2) % len(S)
        print(S[k])

if __name__ == '__main__':
    main()