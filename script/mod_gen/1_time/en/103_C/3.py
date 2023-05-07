def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

if __name__ == '__main__':
    main()