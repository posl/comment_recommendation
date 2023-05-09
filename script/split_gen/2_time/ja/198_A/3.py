def main():
    N = int(input())
    #N=1の時は0を出力
    if N == 1:
        print(0)
    #N=2の時は1を出力
    elif N == 2:
        print(1)
    else:
        #N=3以上の時は、N-1個のお菓子を分け合う方法の数に、
        #A君が一個取り、B君がN-2個取る方法の数を足す
        print(N-1 + main(N-1))
