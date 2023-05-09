def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(sum(A)-N)

if __name__ == '__main__':
    main()