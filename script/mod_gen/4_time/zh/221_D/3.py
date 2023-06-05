def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    # print(ab)
    count = [0] * (10 ** 9 + 2)
    for i in range(n):
        count[ab[i][0]] += 1
        count[ab[i][0] + ab[i][1]] -= 1
    # print(count)
    for i in range(1, 10 ** 9 + 2):
        count[i] += count[i - 1]
    # print(count)
    ans = [0] * (n + 1)
    for i in range(1, 10 ** 9 + 1):
        ans[count[i]] += 1
    # print(ans)
    for i in range(1, n + 1):
        print(ans[i], end=" ")

if __name__ == '__main__':
    main()