def main():
    n = int(input())
    parents = list(map(int, input().split()))
    ans = 0
    current = n
    while current != 1:
        current = parents[current - 2]
        ans += 1
    print(ans)
