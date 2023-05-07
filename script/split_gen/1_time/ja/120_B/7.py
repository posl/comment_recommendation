def main():
    A, B, K = map(int, input().split())
    ans = 0
    i = 0
    while True:
        if A % (A-i) == 0 and B % (A-i) == 0:
            ans = A-i
            K -= 1
        if K == 0:
            break
        i += 1
    print(ans)
