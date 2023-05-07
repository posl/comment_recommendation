def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    print(sum(p) - max(p)//2)

if __name__ == '__main__':
    main()