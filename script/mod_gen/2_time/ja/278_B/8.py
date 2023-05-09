def solve():
    H, M = map(int, input().split())
    if M == 59:
        if H == 23:
            print('0 0')
        else:
            print(str(H+1)+' 0')
    else:
        print(str(H)+' '+str(M+1))

if __name__ == '__main__':
    solve()