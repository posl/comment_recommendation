def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    else:
        print('No')
