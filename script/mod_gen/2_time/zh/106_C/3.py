def problem106_c():
    #S = input()
    #K = int(input())
    S = '299792458'
    K = 9460730472580800
    #print(S)
    #print(K)
    if S[0] == '1':
        print('1')
    elif S[0] == '2':
        if K % 2 == 1:
            print('2')
        else:
            print('3')
    else:
        print(S[0])

if __name__ == '__main__':
    problem106_c()