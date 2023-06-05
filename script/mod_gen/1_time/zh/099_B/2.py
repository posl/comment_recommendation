def main():
    input_line = input()
    input_line = input_line.split(' ')
    a = int(input_line[0])
    b = int(input_line[1])
    if a < 1 or a >= b or b >= 499500:
        print("输入不合法")
        return
    #求出塔的总高度
    total_height = int((1 + 999) * 999 / 2)
    #求出雪覆盖的高度
    snow_height = total_height - (b - a)
    #求出雪覆盖的深度
    snow_depth = b - a - snow_height + 1
    print(snow_depth)

if __name__ == '__main__':
    main()