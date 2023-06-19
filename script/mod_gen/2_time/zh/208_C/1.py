def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    t = K // N
    K = K % N
    for i in range(N):
        if a[i] <= t:
            a[i] = 1
        else:
            a[i] = 0
    for i in range(N):
        if K > 0 and a[i] == 0:
            a[i] = 1
            K -= 1
    for i in range(N):
        print(a[i])
main()
