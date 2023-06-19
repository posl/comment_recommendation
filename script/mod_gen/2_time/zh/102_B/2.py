def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(max(A)-min(A))

if __name__ == '__main__':
    main()