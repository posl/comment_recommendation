def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_num = A[-1]
    check = [True] * (max_num + 1)
    for i in range(N):
        if check[A[i]] == True:
            for j in range(2, max_num // A[i] + 1):
                check[j * A[i]] = False
    ans = 0
    for i in range(N):
        if check[A[i]] == True:
            ans += 1
    print(ans)
