def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [1/a for a in A]
    print(1/sum(A))

if __name__ == '__main__':
    main()