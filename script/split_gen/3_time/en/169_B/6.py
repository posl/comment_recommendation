def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    x = 1
    for a in A:
        x *= a
        if x > 10**18:
            print(-1)
            return
    print(x)
