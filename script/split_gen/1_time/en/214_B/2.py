def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1-a):
            for c in range(S+1-a-b):
                if a*b*c <= T:
                    ans += 1
    print(ans)
