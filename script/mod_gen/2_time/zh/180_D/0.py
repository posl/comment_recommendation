def solution():
    x,y,a,b = map(int,input().split())
    if a == 1:
        if y - x > b:
            print(y - x - 1)
        else:
            print(0)
    else:
        ans = 0
        while x < y:
            if x * a < x + b:
                x *= a
            else:
                x += b
            ans += 1
        print(ans - 1)

if __name__ == '__main__':
    solution()