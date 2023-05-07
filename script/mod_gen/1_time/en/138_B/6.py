def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(1/sum(1/a for a in A))

if __name__ == '__main__':
    main()