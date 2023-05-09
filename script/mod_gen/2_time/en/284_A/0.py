def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N-1, -1, -1):
        print(S[i])

if __name__ == '__main__':
    main()