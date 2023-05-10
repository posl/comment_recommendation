def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    res = 1
    for a in A:
        res *= a
        if res > 10**18:
            print(-1)
            return
    print(res)
    return
