def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if S % N == 0:
        print('Yes')
    else:
        print('No')
