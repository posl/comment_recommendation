def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 'Yes'
    for i in range(M):
        if B[i] not in A:
            ans = 'No'
            break
    print(ans)
