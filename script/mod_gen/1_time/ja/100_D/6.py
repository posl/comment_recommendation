def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: x[i%3]*(-1)**(i//3))
        ans = max(ans, sum(map(abs, [sum(x) for x in zip(*cake[:m])])))
    print(ans)

if __name__ == '__main__':
    main()