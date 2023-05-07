def main():
    #入力
    K = int(input())
    #計算
    #HH = 21 + K // 60
    #MM = K % 60
    HH, MM = divmod(21*60 + K, 60)
    #出力
    print("{:02}:{:02}".format(HH, MM))

if __name__ == '__main__':
    main()