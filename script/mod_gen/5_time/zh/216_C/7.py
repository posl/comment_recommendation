def main():
    n = int(input())
    # 二进制表示
    binary = bin(n)[2:]
    # 二进制表示的长度
    length = len(binary)
    # 二进制表示的长度
    result = ""
    # 二进制表示的长度
    for i in range(length):
        # 二进制表示的长度
        if binary[length - 1 - i] == '1':
            # 二进制表示的长度
            if i % 2 == 0:
                # 二进制表示的长度
                result += "A"
            else:
                # 二进制表示的长度
                result += "B"
    # 二进制表示的长度
    print(result[::-1])

if __name__ == '__main__':
    main()