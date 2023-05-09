def main():
    A, B = map(int, input().split())
    if A > 100 or B > 1000:
        print('Error')
        return
    if A < 1 or B < 1:
        print('Error')
        return
    if A * 6 < B:
        print('No')
        return
    print('Yes')
