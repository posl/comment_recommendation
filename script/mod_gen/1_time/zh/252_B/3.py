def main():
    #输入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #解决问题
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()