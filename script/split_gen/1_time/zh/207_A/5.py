def main():
    try:
        a, b, c = map(int, input().split())
        if a < 1 or a > 100:
            raise Exception('a is not in the range of 1 to 100')
        if b < 1 or b > 100:
            raise Exception('b is not in the range of 1 to 100')
        if c < 1 or c > 100:
            raise Exception('c is not in the range of 1 to 100')
    except Exception as e:
        print(e)
    else:
        print(max(a+b, b+c, a+c))
