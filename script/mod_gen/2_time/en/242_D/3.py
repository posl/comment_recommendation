def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 0:
            print(S[k])
        elif t == 1:
            print(S[k + len(S) // 3])
        else:
            print(S[k + 2 * len(S) // 3])

if __name__ == '__main__':
    main()