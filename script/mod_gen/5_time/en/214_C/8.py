def problem214_c():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T = [0] + T + [0]
    for i in range(1, N+1):
        T[i] = max(T[i], T[i-1]+S[i-1])
    for i in range(1, N+1):
        print(T[i])

if __name__ == '__main__':
    problem214_c()