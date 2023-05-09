def main():
    a,b,x = map(int, input().split())
    ans = 0
    for i in range(1, 10):
        if a * i + b * len(str(i)) <= x:
            ans = max(ans, i)
    print(ans)
