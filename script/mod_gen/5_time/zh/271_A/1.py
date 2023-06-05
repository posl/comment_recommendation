def change2Hex(num):
    if num < 0 or num > 255:
        return "输入数字错误"
    else:
        if num < 16:
            return "0" + hex(num).replace("0x","").upper()
        else:
            return hex(num).replace("0x","").upper()

if __name__ == '__main__':
    change2Hex()