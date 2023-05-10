def main():
    N = int(input())
    ans = N
    for a in range(2, int(N**0.5)+1):
        x = a*a
        while x <= N:
            ans -= 1
            x *= a
    print(ans)
