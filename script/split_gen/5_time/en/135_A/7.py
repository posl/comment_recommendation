def main():
    a,b = map(int, input().split())
    k = (a + b) // 2
    print(k if (a - k) == (k - b) else 'IMPOSSIBLE')
