def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * len([x for x in range(1, i+1) if i % x == 0])
    print(ans)
