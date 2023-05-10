def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        exit()
    p = 1
    for i in A:
        p *= i
        if p > 10**18:
            print(-1)
            exit()
    print(p)
    exit()
