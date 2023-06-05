def solve():
    n = int(input())
    height = list(map(int, input().split()))
    max_height = 0
    count = 0
    for i in range(n):
        if height[i] >= max_height:
            max_height = height[i]
            count += 1
    print(count)

if __name__ == '__main__':
    solve()