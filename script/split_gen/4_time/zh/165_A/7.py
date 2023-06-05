def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print('OK')
        return
    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            return
    print('NG')
