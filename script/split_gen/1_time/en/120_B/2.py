def main():
    A, B, K = map(int, input().split())
    ans = 0
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            K -= 1
            if K == 0:
                ans = i
                break
    print(ans)
