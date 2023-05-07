def solve():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1, 29):
        for j in range(1, 29):
            for k in range(1, 29):
                if h[0] == i + j + k and h[1] == i + 2 * j + 3 * k and h[2] == 2 * i + 3 * j + 4 * k and w[0] == i + 2 * k and w[1] == j + 3 * k and w[2] == k + 2 * k:
                    ans += 1
    print(ans)
solve()
Hi, I'm a beginner in programming and I'm learning python. I'm trying to make a program that will calculate the factorial of a number. I'm trying to use recursion but I'm not sure how to code it. I've tried to use recursion but I keep getting errors. Here's my code:
