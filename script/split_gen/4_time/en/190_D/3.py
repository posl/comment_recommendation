def main():
    n = int(input())
    ans = 0
    for i in range(1, 10**6):
        if n - i*(i+1)//2 < 0:
            break
        if (n - i*(i+1)//2) % i == 0:
            ans += 2
    print(ans)
