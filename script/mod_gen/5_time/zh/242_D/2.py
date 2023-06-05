def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 0:
            print(S[k])
        elif t == 1:
            print(S[k % 3 + 1] if S[k] == 'a' else S[k % 3 - 1])
        else:
            print(S[k % 3 - 1] if S[k] == 'c' else S[k % 3 + 1])

if __name__ == '__main__':
    main()