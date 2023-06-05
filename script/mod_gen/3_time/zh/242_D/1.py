def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t = t % 3
        if t == 0:
            print(S[k - 1])
        elif t == 1:
            print(S[k % 3 - 1])
        elif t == 2:
            print(S[(k + 1) % 3 - 1])

if __name__ == '__main__':
    main()