def main():
    N = int(input())
    if N < 4:
        print('No')
    elif N == 4 or N == 7:
        print('Yes')
    else:
        if N % 4 == 0 or N % 7 == 0 or N % 4 == 7 or N % 7 == 4:
            print('Yes')
        else:
            print('No')
