def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
            return
        else:
            print(0)
            return
    else:
        def convert_base(x, base):
            if int(x) == 0:
                return 0
            else:
                digits = []
                while x:
                    digits.append(int(x % base))
                    x //= base
                digits.reverse()
                return int(''.join(map(str, digits)))
        n = d + 1
        while True:
            if convert_base(x, n) <= m:
                n += 1
            else:
                print(n - d - 1)
                return

if __name__ == '__main__':
    main()