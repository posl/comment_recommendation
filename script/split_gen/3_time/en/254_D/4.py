def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            if i*j == int(i*j**0.5)**2:
                ans += 1
    print(ans)
