def main():
    a,b = map(int, input().split())
    c = 1
    while True:
        if a == b:
            print(c)
            exit()
        else:
            if a > b:
                b += 2 ** c
            else:
                a += 2 ** c
        c += 1
