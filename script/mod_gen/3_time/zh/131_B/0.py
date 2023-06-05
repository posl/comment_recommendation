def main():
    N, L = map(int, input().split())
    taste = [L + i for i in range(N)]
    print(sum(taste) - min(taste, key=abs))

if __name__ == '__main__':
    main()