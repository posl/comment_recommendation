def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    #sum_{i=1}^{M} i × B_i の最大値を求める
    #B=(B_1,B_2,...,B_M)
    #sum_{i=1}^{M} i × B_i = sum_{i=1}^{M} i × A_{i+j-1}
    #i+j-1がM以下であるi,jの組み合わせを全て試す
    #i+j-1がM以下であるi,jの組み合わせの個数は、
    #i+j-1がM以下のiの個数×jの個数
    #iが1からMまでの時、i+j-1がM以下のjの個数は、
    #M-(i+j-1)+1=M-i+1
    #よって、sum_{i=1}^{M} i × B_i = sum_{i=1}^{M} i × A_{i+j-1} = sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1}
    #sum_{i=1}^{M} i × B_i の最大値は、
    #sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1} の最大値
    #sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1} = sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1}
    #sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1} の最大値を求める
    #sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1}

if __name__ == '__main__':
    main()