def func():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #print(H)
    min = 100000
    ans = 0
    for i in range(N):
        tmp = T - H[i] * 0.006
        if abs(A - tmp) < min:
            min = abs(A - tmp)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    func()