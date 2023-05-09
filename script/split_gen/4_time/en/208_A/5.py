def main():
    a, b = map(int, input().split())
    print('Yes' if a * 6 >= b and a <= b else 'No')
