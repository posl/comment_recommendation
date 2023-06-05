def main():
    while True:
        try:
            N = int(input('请输入一个1到100之间的整数：'))
            if 1 <= N <= 100:
                break
            else:
                print('输入的数不在范围内，请重新输入')
        except:
            print('输入的数不是整数，请重新输入')
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    elif N % 4 == 3 or N % 7 == 3 or N % 11 == 3:
        print('No')
    else:
        print('Yes')
