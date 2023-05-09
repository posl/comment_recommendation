def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    s = ""
    while n != 0:
        if n%2 == 0:
            s = "0" + s
        else:
            s = "1" + s
            n -= 1
        n //= -2
    print(s)
