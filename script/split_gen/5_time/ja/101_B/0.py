def main():
    N = int(input())
    sn = sum([int(x) for x in str(N)])
    if N % sn == 0:
        print('Yes')
    else:
        print('No')
