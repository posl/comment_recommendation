def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            if i*j > N:
                break
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans)
