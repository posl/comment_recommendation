def main():
    # 读入
    input = raw_input()
    # 分割
    input_list = input.split()
    # 判断
    if input_list[0] == input_list[1] == input_list[2]:
        print "Won"
    else:
        print "Lost"

if __name__ == '__main__':
    main()