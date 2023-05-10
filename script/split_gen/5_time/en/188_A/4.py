def main():
    x, y = map(int, input().split())
    print('Yes' if x < y and x + 3 > y else 'No')
