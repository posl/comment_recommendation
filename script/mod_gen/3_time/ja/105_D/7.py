def  main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod_A = [0] * (N + 1)
    for i in range(N):
        mod_A[i + 1] = (mod_A[i] + A[i]) % M
    mod_A.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if mod_A[i] == mod_A[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

if __name__ == '__main__':
    ()