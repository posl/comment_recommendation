def main():
    K = int(input())
    A, B = map(int, input().split())
    if (A % K == 0) or (B % K == 0):
        print('OK')
    else:
        for i in range(A, B+1):
            if i % K == 0:
                print('OK')
                return
        print('NG')
