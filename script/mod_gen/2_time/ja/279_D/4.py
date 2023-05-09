def main():
    import math
    A,B = map(int,input().split())
    #A = 1000000000000000000
    #B = 100
    g = 1
    t = 0
    while True:
        t += B
        g += 1
        if A/((g)**(1/2)) <= t:
            break
    print(t)

if __name__ == '__main__':
    main()