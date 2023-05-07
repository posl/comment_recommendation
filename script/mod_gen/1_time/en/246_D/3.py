def main():
    n = int(input())
    for i in range(n, n+100):
        for a in range(0, 1000):
            for b in range(0, 1000):
                if i == a**3 + a**2*b + a*b**2 + b**3:
                    print(i)
                    return
main()
I got TLE for the 3rd sample input. I'm not sure what I'm doing wrong. I tried to make it more efficient by reducing the range of a and b, but no luck.
I'm not sure if it's possible to make it more efficient, but I think it's possible to make it more efficient. I think it's possibl

if __name__ == '__main__':
    main()