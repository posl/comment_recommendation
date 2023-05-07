def main():
    k = int(input())
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            return
    print('NG')
