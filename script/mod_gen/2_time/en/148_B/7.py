def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], end='')
    print()

if __name__ == '__main__':
    main()