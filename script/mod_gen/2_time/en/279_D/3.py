def main():
    a,b = map(int,input().split())
    g = 1
    t = 0
    while True:
        if a/g**0.5 <= t:
            print(t)
            return
        t += b
        g += 1
main()
