def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    print(sum(A[:-1]))

if __name__ == '__main__':
    main()