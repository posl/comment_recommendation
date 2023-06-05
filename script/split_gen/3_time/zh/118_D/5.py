def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = []
    for i in range(M):
        for j in range(A[i]):
            ans.append(str(i+1))
    print(''.join(ans))
