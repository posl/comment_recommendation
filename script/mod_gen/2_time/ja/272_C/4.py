def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    elif A[-2] % 2 == 0:
        print(A[-2])
    else:
        print(-1)

if __name__ == '__main__':
    main()