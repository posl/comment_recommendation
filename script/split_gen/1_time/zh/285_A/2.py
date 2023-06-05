def main():
    a, b = map(int, input().split())
    if a in [1, 3, 5, 7, 9, 11, 13, 15] and b in [2, 4, 6, 8, 10, 12, 14]:
        print('Yes')
    else:
        print('No')
