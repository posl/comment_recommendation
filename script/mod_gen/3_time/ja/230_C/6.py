def main():
    #入力
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #黒マスの数を求める
    #黒マスの数 = 黒マスの数A + 黒マスの数B - 重複する黒マスの数
    #黒マスの数A = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #黒マスの数B = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #重複する黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) // 2 * 2
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) // 6
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) // 24
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) * (min(N-A,N-B)+5) // 120
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+4) * (min(N-A,N-B)+5) * (min(N-A,N-B)+6) // 720
    #黒マスの数 = (min(N-A,N-B)+1) * (min(N-A,N-B)+2) * (min(N-A,N-B)+3) * (min(N-A,N-B)+

if __name__ == '__main__':
    main()