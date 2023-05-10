def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j > N:
                break
            else:
                ans += 1
    print(ans)
