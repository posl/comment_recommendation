def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(N):
        K, *A = map(int, input().split())
        if i == 0:
            ans = set(A)
        else:
            ans = ans & set(A)
    print(len(ans))
