def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 1
    if 0 in A:
        print(0)
    else:
        for a in A:
            result *= a
            if result > 10**18:
                print(-1)
                exit()
        print(result)
