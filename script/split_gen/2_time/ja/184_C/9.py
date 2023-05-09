def solve():
    # ここに書いてね
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
        print(0)
        return
    if abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        return
    if r1+c1 == r2+c2 or r1-c1 == r2-c2:
        print(1)
        return
    if (r1+c1+r2+c2)%2 == 0:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i)+abs(j) <= 3:
                if (r1+i)+(c1+j) == r2+c2 or (r1+i)-(c1+j) == r2-c2:
                    print(2)
                    return
    print(3)
    return
