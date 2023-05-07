def main():
    A,B = map(int,input().split())
    import math
    g = 1
    time = A/math.sqrt(g)
    while True:
        g += 1
        time = min(time, B+ A/math.sqrt(g))
        if time == B:
            break
    print(time)

if __name__ == '__main__':
    main()