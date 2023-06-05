def main():
    x, y = map(int, input().split())
    ans = 0
    for i in range(0, 10):
        if x + i * 10 >= y:
            ans = i
            break
    print(ans)
