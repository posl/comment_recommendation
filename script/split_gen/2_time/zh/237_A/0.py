def main():
    # 你的代码写在这里
    n = int(input())
    if -2 ** 31 <= n <= 2 ** 31 - 1:
        print('是')
    else:
        print('否')
