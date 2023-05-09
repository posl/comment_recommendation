def main():
    N = int(input())
    ans = 0
    for a in range(1, int(N**(1/3))+1):
        for b in range(a, int(N**(1/2))+1):
            for c in range(b, N+1):
                if a*b*c > N:
                    break
                ans += 1
    print(ans)
