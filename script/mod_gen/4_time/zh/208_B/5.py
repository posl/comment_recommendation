def cal(n):
    if n == 1:
        return 1
    return n * cal(n-1)

if __name__ == '__main__':
    cal()