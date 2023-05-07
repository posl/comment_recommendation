def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - 10 for a in A if a > 10]
    print(sum(A))

if __name__ == '__main__':
    main()