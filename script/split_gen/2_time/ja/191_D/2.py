def main():
    x, y, r = map(float, input().split())
    ans = 0
    for i in range(int(x-r), int(x+r)+1):
        for j in range(int(y-r), int(y+r)+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                ans += 1
    print(ans)
