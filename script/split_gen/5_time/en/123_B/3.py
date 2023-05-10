def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_time = min(a, b, c, d, e)
    if a % 10 == 0:
        a_time = a
    else:
        a_time = (a // 10 + 1) * 10
    if b % 10 == 0:
        b_time = b
    else:
        b_time = (b // 10 + 1) * 10
    if c % 10 == 0:
        c_time = c
    else:
        c_time = (c // 10 + 1) * 10
    if d % 10 == 0:
        d_time = d
    else:
        d_time = (d // 10 + 1) * 10
    if e % 10 == 0:
        e_time = e
    else:
        e_time = (e // 10 + 1) * 10
    time = a_time + b_time + c_time + d_time + e_time - min_time
    print(time)
