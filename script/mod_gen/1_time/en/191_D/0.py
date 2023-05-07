def main():
    x, y, r = map(float, input().split())
    x = int(x*10000+0.5)
    y = int(y*10000+0.5)
    r = int(r*10000+0.5)
    ans = 0
    for i in range(-r, r+1):
        if i*i > r*r:
            break
        j = int((r*r-i*i)**0.5)
        ans += 1+2*j
        if i == 0:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()