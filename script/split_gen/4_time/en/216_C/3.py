def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s = "B" + s
            n = n // 2
        else:
            s = "A" + s
            n -= 1
    print(s)
