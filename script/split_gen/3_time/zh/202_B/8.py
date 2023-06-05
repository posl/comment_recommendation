def main():
    # 读入
    s = input()
    # 处理
    s2 = s[::-1]
    s3 = ""
    for i in range(len(s2)):
        if s2[i] == "0":
            s3 = s3 + "0"
        elif s2[i] == "1":
            s3 = s3 + "1"
        elif s2[i] == "6":
            s3 = s3 + "9"
        elif s2[i] == "8":
            s3 = s3 + "8"
        elif s2[i] == "9":
            s3 = s3 + "6"
    # 输出
    print(s3)
