def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            ans += 1
    print(ans)
