def main():
    N = int(input())
    if N >= 1 and N <= 9:
        print('AGC00' + str(N))
    elif N >= 10 and N <= 99:
        print('AGC0' + str(N))
    else:
        print('AGC' + str(N))
