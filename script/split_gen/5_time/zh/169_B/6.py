def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit(0)
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            exit(0)
    print(ans)
