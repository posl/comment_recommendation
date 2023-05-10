def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    ans = 0
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    for i in range(N):
        for j in range(N):
            if A[i] == 0:
                continue
            if A[j] == 0:
                continue
            if A[i] == A[j]:
                ans += dic[A[i]] - 1
            else:
                if A[i] > A[j]:
                    if A[i] % A[j] == 0:
                        if A[i] // A[j] in dic:
                            ans += dic[A[i] // A[j]]
                else:
                    if A[j] % A[i] == 0:
                        if A[j] // A[i] in dic:
                            ans += dic[A[j] // A[i]]
    print(ans // 2)
