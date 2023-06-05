def main():
    N = int(input())
    ans = N
    for b in range(2, int(N**0.5)+1):
        for a in range(2, int(N**0.5)+1):
            if a**b <= N:
                ans -= 1
            else:
                break
    print(ans)
