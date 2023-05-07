def main():
    K = int(input())
    #21時ちょうどからの経過時間
    time = 21 * 60 + K
    #24時間制の時間
    hour = time // 60
    #分
    minute = time % 60
    print("{0:02}:{1:02}".format(hour, minute))

if __name__ == '__main__':
    main()