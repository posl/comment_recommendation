def cnt_step(r, x, y):
    if r**2 == x**2 + y**2:
        return int(r)
    elif r**2 > x**2 + y**2:
        return int(r+1)
    else:
        cnt = 0
        while True:
            if r**2 == x**2 + y**2:
                return int(cnt)
            elif r**2 > x**2 + y**2:
                return int(cnt+2)
            else:
                cnt += 2
                r += 1
r, x, y = map(int, input().split())
print(cnt_step(r, x, y))

if __name__ == '__main__':
    cnt_step()