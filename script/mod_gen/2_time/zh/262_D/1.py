def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i
    ans = 0
    min_pos = n
    max_pos = -1
    for i in range(n):
        min_pos = min(min_pos, b[i])
        max_pos = max(max_pos, b[i])
        if max_pos - min_pos == i:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()