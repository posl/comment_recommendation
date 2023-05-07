def main():
    k = int(input())
    h = 21
    m = 0
    m += k
    while m >= 60:
        m -= 60
        h += 1
    print(str(h) + ":" + str(m).zfill(2))
main()
