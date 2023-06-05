def main():
    str = input("输入N i：")
    strlist = str.split()
    N = int(strlist[0])
    i = int(strlist[1])
    j = N - i + 1
    print(j)
