def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 1. Find the ladders that connect the highest floor (10**9)
    # 2. Find the ladders that connect the highest floor (10**9) from those ladders
    # 3. Repeat step 2 until there is no ladder that connects the highest floor (10**9)
    # 4. The highest floor that Takahashi can reach is the highest floor of the ladders that connect the highest floor (10**9)
    ladders = set(range(N))
    while True:
        next_ladders = set()
        for i in ladders:
            a, b = AB[i]
            if a == 10**9 or b == 10**9:
                next_ladders.add(i)
        if len(next_ladders) == 0:
            break
        ladders = next_ladders
    ans = 10**9
    for i in ladders:
        a, b = AB[i]
        ans = min(ans, a, b)
    print(ans)

if __name__ == '__main__':
    main()