def check():
    #K
    k = int(input())
    #A B
    a,b = map(int, input().split())
    if a%k == 0 or b%k == 0:
        print('OK')
    elif a//k != b//k:
        print('OK')
    else:
        print('NG')
