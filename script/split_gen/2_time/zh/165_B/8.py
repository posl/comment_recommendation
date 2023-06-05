def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0:
        print('OK')
    elif b // k > a // k:
        print('OK')
    else:
        print('NG')
