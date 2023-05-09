def main():
    x, y, r = map(float, input().split())
    x, y = int(x*10000), int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r, x+r+1):
        if i < 0 or i > 10**5:
            continue
        h = (r**2 - (x-i)**2)**0.5
        ans += int(y+h)//10000 - max(0, (y-h)//10000) + 1
    print(ans)

if __name__ == '__main__':
    main()