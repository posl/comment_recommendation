def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    a = [[0 for i in range(2)] for j in range(N)]
    for i in range(N):
        a[i][0] = S[i]
        a[i][1] = T[i]
    a.sort(key=lambda x:x[1])
    for i in range(N):
        print(a[i][0])
