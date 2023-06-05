def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    result = 1
    for i in range(n):
        result *= a[i]
        if result > 10**18:
            print(-1)
            return
    print(result)
    return
