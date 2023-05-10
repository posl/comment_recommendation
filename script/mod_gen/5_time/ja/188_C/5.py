def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = A.copy()
    B.sort()
    print(A.index(B[-2]) + 1)
main()

if __name__ == '__main__':
    main()