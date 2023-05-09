def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        for j in range(t, -1, -1):
            if k > 2**j:
                k -= 2**j
                if S[j] == 'A':
                    S[j] = 'B'
                elif S[j] == 'B':
                    S[j] = 'C'
                elif S[j] == 'C':
                    S[j] = 'A'
        print(S[k-1])

if __name__ == '__main__':
    main()