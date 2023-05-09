def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s = sum(A)
    if s < 0:
        print(s + 2 * A[0])
    elif s == 0:
        print(2 * A[0])
    else:
        print(s - 2 * A[0])

if __name__ == '__main__':
    main()