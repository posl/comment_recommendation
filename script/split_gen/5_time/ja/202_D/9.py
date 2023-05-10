def main():
    a, b, k = map(int, input().split())
    s = ''
    for i in range(a + b):
        if a == 0:
            s += 'b'
            b -= 1
            continue
        if b == 0:
            s += 'a'
            a -= 1
            continue
        if k <= num(a - 1, b):
            s += 'a'
            a -= 1
        else:
            s += 'b'
            k -= num(a - 1, b)
            b -= 1
    print(s)
