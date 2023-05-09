def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    ans = 0
    for A, B in ladders:
        if ans < A:
            ans = B
    print(ans)

if __name__ == '__main__':
    main()