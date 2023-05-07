def main():
    N = int(input())
    x = 0
    y = 0
    ans = 0
    while True:
        ans += 1
        if x < y:
            x += 1
        else:
            y += 1
        if x * y >= N:
            break
    print(ans)
