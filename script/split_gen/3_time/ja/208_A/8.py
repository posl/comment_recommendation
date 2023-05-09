def main():
    A, B = map(int, input().split())
    if A * 6 >= B and A <= B:
        print('Yes')
    else:
        print('No')
