def main():
    N = int(input())
    ans = N
    while True:
        for a in range(1000):
            for b in range(1000):
                if ans == a**3 + a**2*b + a*b**2 + b**3:
                    print(ans)
                    return
        ans += 1
