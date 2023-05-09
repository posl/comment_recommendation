def main():
    #入力
    P = list(map(int,input().split()))
    #A-Zをリストに格納
    A = [chr(i) for i in range(97,123)]
    #出力
    print(''.join([A[i-1] for i in P]))

if __name__ == '__main__':
    main()