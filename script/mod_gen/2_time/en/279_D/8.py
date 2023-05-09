def main():
    import math
    a,b = map(int,input().split())
    g = 1
    ans = a * (g**(-0.5))
    while True:
        g += 1
        t = b + a * (g**(-0.5))
        if t < ans:
            ans = t
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()