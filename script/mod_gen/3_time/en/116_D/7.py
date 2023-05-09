def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    ans = 0
    tmp = 0
    for i in range(k):
        ans += sushi[i][1]
        kind.add(sushi[i][0])
        tmp += 1
    ans += tmp * tmp
    for i in range(k, n):
        if sushi[i][0] not in kind:
            for j in range(k):
                if sushi[j][0] not in kind:
                    if sushi[j][1] < sushi[i][1]:
                        kind.remove(sushi[j][0])
                        kind.add(sushi[i][0])
                        ans = ans - sushi[j][1] + sushi[i][1] + 2 * tmp - 1
                        sushi[j][1] = sushi[i][1]
                        break
    print(ans)

if __name__ == '__main__':
    main()