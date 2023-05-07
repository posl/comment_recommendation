def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    print(N-1)
    for i in range(N-1):
        print(i%N)

if __name__ == '__main__':
    main()