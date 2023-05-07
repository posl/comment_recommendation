def main():
    N = int(input())
    S = 0
    while N > 0:
        S += N % 10
        N = N // 10
    if S % 2 == 0:
        print('Yes')
    else:
        print('No')
