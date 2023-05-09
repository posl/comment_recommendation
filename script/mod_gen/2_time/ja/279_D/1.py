def main():
    A,B = map(int,input().split())
    g = 1
    t = 0
    while True:
        if A/(g**0.5) < t:
            break
        t += B
        g += 1
    print(t)

if __name__ == '__main__':
    main()