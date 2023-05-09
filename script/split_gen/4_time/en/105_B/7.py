def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    elif N >= 8 and N % 4 == 3 or N % 7 == 3:
        print('Yes')
    elif N >= 15 and N % 4 == 7 or N % 7 == 7:
        print('Yes')
    elif N >= 22 and N % 4 == 11 or N % 7 == 11:
        print('Yes')
    else:
        print('No')
