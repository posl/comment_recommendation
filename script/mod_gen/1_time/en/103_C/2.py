def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A) - N
    print(ans)

if __name__ == '__main__':
    main()