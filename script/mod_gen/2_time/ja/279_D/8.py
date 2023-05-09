def main():
    A,B = map(int,input().split())
    g = 1
    t = 0
    while True:
        if t + A/((g)**(1/2)) < 1 + t + B:
            print(t + A/((g)**(1/2)))
            return
        else:
            g += 1
            t += B

if __name__ == '__main__':
    main()