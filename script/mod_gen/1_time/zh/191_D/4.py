def main():
    x, y, r = map(float, input().split())
    x, y, r = int(x*10000), int(y*10000), int(r*10000)
    ans = 0
    for i in range(-r, r+1):
        j = int((r**2 - i**2)**0.5)
        while i**2 + j**2 > r**2:
            j -= 1
        ans += j*2+1
    print(ans*4)

if __name__ == '__main__':
    main()