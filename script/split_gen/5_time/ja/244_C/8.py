def main():
    n = int(input())
    a = 1
    b = 2*n
    while True:
        print(a)
        a += 1
        c = int(input())
        if c == 0:
            break
        if c == b:
            a = b
            b -= 1
