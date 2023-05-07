def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0 or (A // K + 1) * K <= B:
        print('OK')
    else:
        print('NG')
