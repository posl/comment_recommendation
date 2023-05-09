def main():
    A,B,C,D = map(int,input().split())
    # A,B,C,D = 4,9,2,3
    # A,B,C,D = 10,40,6,8
    # A,B,C,D = 314159265358979323,846264338327950288,419716939,937510582
    # 全体の数
    all_num = B - A + 1
    # Cで割り切れる数
    C_num = B // C - (A-1) // C
    # Dで割り切れる数
    D_num = B // D - (A-1) // D
    # CとDで共通に割り切れる数
    CD_num = B // (C*D) - (A-1) // (C*D)
    print(all_num - C_num - D_num + CD_num)

if __name__ == '__main__':
    main()