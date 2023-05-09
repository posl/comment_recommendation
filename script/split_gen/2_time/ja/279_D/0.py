def main():
    A, B = map(int, input().split())
    g = 1
    ans = 10**18
    for i in range(B+1):
        ans = min(ans, i + A/((g+i)**0.5))
    print(ans)
