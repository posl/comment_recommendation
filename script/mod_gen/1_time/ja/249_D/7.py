def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    count = [0] * (A[-1]+1)
    for i in A:
        count[i] += 1
    ans = 0
    for i in A:
        if i == 0:
            continue
        for j in A:
            if i > j:
                continue
            if i == j:
                ans += (count[i] * (count[i]-1)) // 2
                break
            if (i * j) % (i - j) == 0:
                k = (i * j) // (i - j)
                if k in A:
                    ans += count[i] * count[j]
    print(ans)

if __name__ == '__main__':
    main()