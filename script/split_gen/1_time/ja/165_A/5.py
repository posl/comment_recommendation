def main():
    # input
    K = int(input())
    A, B = map(int, input().split())
    # compute
    # output
    if A%K==0 or B%K==0:
        print('OK')
    elif A//K != B//K:
        print('OK')
    else:
        print('NG')
