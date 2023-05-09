def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

if __name__ == '__main__':
    main()