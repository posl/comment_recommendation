Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    time = 0
    
    if a % 10 != 0:
        time += a - (a % 10) + 10
    else:
        time += a
    time += b - (b % 10) + 10
    time += c - (c % 10) + 10
    time += d - (d % 10) + 10
    time += e - (e % 10) + 10
    
    print(time)

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a,b,c,d,e]
    time.sort()
    time.reverse()
    print(time[0])

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    
    array = [A, B, C, D, E]
    max_time = max(array)
    if max_time % 10 == 0:
        print(max_time)
    else:
        print(max_time + (10 - max_time % 10))

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min = A
    if B < min:
        min = B
    if C < min:
        min = C
    if D < min:
        min = D
    if E < min:
        min = E

    if A % 10 == 0:
        A = A
    else:
        A = (A // 10 + 1) * 10
    if B % 10 == 0:
        B = B
    else:
        B = (B // 10 + 1) * 10
    if C % 10 == 0:
        C = C
    else:
        C = (C // 10 + 1) * 10
    if D % 10 == 0:
        D = D
    else:
        D = (D // 10 + 1) * 10
    if E % 10 == 0:
        E = E
    else:
        E = (E // 10 + 1) * 10

    print(A + B + C + D + E - 10 + min)

=======
Suggestion 5

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    result = 0
    if A % 10 != 0:
        A = (A // 10 + 1) * 10
    if B % 10 != 0:
        B = (B // 10 + 1) * 10
    if C % 10 != 0:
        C = (C // 10 + 1) * 10
    if D % 10 != 0:
        D = (D // 10 + 1) * 10
    if E % 10 != 0:
        E = (E // 10 + 1) * 10
    result = A + B + C + D + E
    print(result)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    list = [a,b,c,d,e]
    list.sort()
    print(list[4] + (10 - list[4]%10) + list[3] + (10 - list[3]%10) + list[2] + (10 - list[2]%10) + list[1] + (10 - list[1]%10) + list[0] + (10 - list[0]%10))

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += (a // 10) * 10
    if a % 10 != 0:
        ans += 10
    ans += (b // 10) * 10
    if b % 10 != 0:
        ans += 10
    ans += (c // 10) * 10
    if c % 10 != 0:
        ans += 10
    ans += (d // 10) * 10
    if d % 10 != 0:
        ans += 10
    ans += (e // 10) * 10
    if e % 10 != 0:
        ans += 10
    print(ans)

=======
Suggestion 8

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    a = (a+9)//10*10
    b = (b+9)//10*10
    c = (c+9)//10*10
    d = (d+9)//10*10
    e = (e+9)//10*10

    print(a+b+c+d+e)

=======
Suggestion 9

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        pass
    else:
        a = (a//10+1)*10
    if b%10 == 0:
        pass
    else:
        b = (b//10+1)*10
    if c%10 == 0:
        pass
    else:
        c = (c//10+1)*10
    if d%10 == 0:
        pass
    else:
        d = (d//10+1)*10
    if e%10 == 0:
        pass
    else:
        e = (e//10+1)*10
    print(a+b+c+d+e)

=======
Suggestion 10

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    # 10の倍数の時刻で注文する
    # 10の倍数の時刻で届く
    dish = [a, b, c, d, e]
    dish.sort()
    dish[0] = dish[0] + 10 - dish[0] % 10
    dish[1] = dish[1] + 10 - dish[1] % 10
    dish[2] = dish[2] + 10 - dish[2] % 10
    dish[3] = dish[3] + 10 - dish[3] % 10
    dish[4] = dish[4] + 10 - dish[4] % 10
    print(dish[0] + dish[1] + dish[2] + dish[3] + dish[4])
