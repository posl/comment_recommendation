def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_ = min(a, b, c, d, e)
    if n % min_ == 0:
        print(n // min_ + 4)
    else:
        print(n // min_ + 1 + 4)

if __name__ == '__main__':
    main()