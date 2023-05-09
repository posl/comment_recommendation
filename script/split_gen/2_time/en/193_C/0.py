def main():
    n = int(input())
    ans = 0
    for a in range(2, int(n**0.5)+1):
        for b in range(2, int(n**0.5)+1):
            if a**b <= n:
                ans += 1
            else:
                break
    print(n-ans)
