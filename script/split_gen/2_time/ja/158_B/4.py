def main():
    n, a, b = map(int, input().split())
    #print(n, a, b)
    ans = (n // (a + b)) * a + min(n % (a + b), a)
    print(ans)
