def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 1:
        print(-1)
    else:
        print(A[-1] + A[-2])

if __name__ == '__main__':
    main()