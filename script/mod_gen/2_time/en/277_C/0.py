def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[0], reverse=True)
    ans = 1
    for a, b in ladders:
        if a <= ans:
            ans = b
        elif b <= ans:
            ans = a
    print(ans)

if __name__ == '__main__':
    main()