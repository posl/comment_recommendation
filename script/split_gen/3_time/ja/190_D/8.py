def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if n/i - i/2 > 0 and (n/i - i/2) % 1 == 0:
            ans += 1
    print(ans*2)
