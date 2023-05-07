def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a % M for a in A]
    A = [a for a in A if a != 0]
    A = [M - a for a in A]
    A.sort()
    print(sum(A))

if __name__ == '__main__':
    main()