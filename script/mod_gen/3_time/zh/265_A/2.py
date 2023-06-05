def buy_apple(x, y, n):
    # 用x买
    if n % 3 == 0:
        return x * n // 3
    else:
        # 用y买
        if n % 3 == 1:
            return min(x*(n-1)//3 + y, x*(n-2)//3 + 2*y)
        else:
            return min(x*(n-2)//3 + 2*y, x*(n-1)//3 + y)

if __name__ == '__main__':
    buy_apple()