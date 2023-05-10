def main():
    A, B = map(int, input().split())
    if A*1 <= B and A*6 >= B:
        print('Yes')
    else:
        print('No')
