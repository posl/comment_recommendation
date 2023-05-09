def main():
    n = int(input())
    if -2147483648 <= n and n < 2147483648:
        print('Yes')
    else:
        print('No')
