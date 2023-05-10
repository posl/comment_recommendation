def main():
    n = int(input())
    s = list(map(int, input().split()))
    result = 0
    for i in range(n):
        a = 1
        while True:
            b = 1
            while True:
                if (4*a*b+3*a+3*b) == s[i]:
                    result += 1
                    break
                elif (4*a*b+3*a+3*b) > s[i]:
                    break
                b += 1
            if b == 1:
                break
            a += 1
    print(n-result)

if __name__ == '__main__':
    main()