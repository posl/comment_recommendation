def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        print(T[i] - S[i])

if __name__ == '__main__':
    main()