def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort()
    print(ladders[-1][1])

if __name__ == '__main__':
    main()