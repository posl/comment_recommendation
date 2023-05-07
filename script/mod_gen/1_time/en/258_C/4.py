def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 2:
            print(S[x-1])
        else:
            S = S[-x:] + S[:-x]
main()

if __name__ == '__main__':
    main()