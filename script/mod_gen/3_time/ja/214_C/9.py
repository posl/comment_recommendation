def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T2 = list(T)
    for i in range(N):
        T2[(i+1)%N] = min(T2[(i+1)%N], T2[i] + S[i])
    for i in range(N):
        T[i] = min(T[i], T2[(i-1)%N] + S[(i-1)%N])
    for i in range(N):
        print(T[i])

if __name__ == '__main__':
    main()