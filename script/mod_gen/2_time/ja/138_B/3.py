def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum(1/a for a in A))

if __name__ == '__main__':
    main()