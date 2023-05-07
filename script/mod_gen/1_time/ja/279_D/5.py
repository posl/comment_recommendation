def main():
    import math
    a,b = map(int,input().split())
    g = 1
    t = 0
    while True:
        t += b
        g += 1
        if t + (a/math.sqrt(g)) <= t:
            break
    print(t + (a/math.sqrt(g)))

if __name__ == '__main__':
    main()