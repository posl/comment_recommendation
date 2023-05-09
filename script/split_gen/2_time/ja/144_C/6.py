def main():
    N = int(input())
    x, y = 1, 1
    ans = 0
    while x != N:
        if (x+1)*(y+1) <= N:
            x += 1
            y += 1
        elif (x+1)*y <= N:
            x += 1
        elif x*(y+1) <= N:
            y += 1
        else:
            x -= 1
        ans += 1
    print(ans)
