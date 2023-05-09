def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_time = min(a,b,c,d,e)
    time = 0
    if a % 10 != 0:
        time += (a//10 + 1) * 10
    else:
        time += a
    if b % 10 != 0:
        time += (b//10 + 1) * 10
    else:
        time += b
    if c % 10 != 0:
        time += (c//10 + 1) * 10
    else:
        time += c
    if d % 10 != 0:
        time += (d//10 + 1) * 10
    else:
        time += d
    if e % 10 != 0:
        time += (e//10 + 1) * 10
    else:
        time += e
    time -= 10
    print(time)
