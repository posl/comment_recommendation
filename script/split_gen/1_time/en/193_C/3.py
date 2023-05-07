def main():
    N = int(input())
    ans = 0
    for a in range(2, N+1):
        for b in range(2, N+1):
            if N >= a**b:
                ans += 1
            else:
                break
    print(N-ans)
