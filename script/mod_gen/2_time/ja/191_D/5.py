def main():
    x,y,r = map(float, input().split())
    r = int(r)
    cnt = 0
    for i in range(-r, r+1):
        cnt += int((r**2 - (x-i)**2)**0.5)
    print(cnt*4+1)

if __name__ == '__main__':
    main()