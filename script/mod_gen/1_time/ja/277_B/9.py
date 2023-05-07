def main():
    #入力
    N = int(input())
    S = [input() for i in range(N)]
    
    #出力
    if len(set(S)) == N and all(s[0] in 'HDCS' and s[1] in 'A23456789TJQK' for s in S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()