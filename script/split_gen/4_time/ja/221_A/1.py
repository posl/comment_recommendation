def main():
    A, B = map(int, input().split())
    ans = 1
    for i in range(B, A):
        ans *= 32
    print(ans)
