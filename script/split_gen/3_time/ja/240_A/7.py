def main():
    a, b = map(int, input().split())
    if a <= 3 <= b or a <= 7 <= b:
        print('Yes')
    else:
        print('No')
