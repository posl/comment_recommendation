def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    elif A[-1] % 2 == 1:
        if A[-2] % 2 == 0:
            print(A[-2])
        else:
            print(-1)
main()
