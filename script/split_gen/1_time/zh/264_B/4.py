def main():
    #读取输入
    r,c = map(int,input().split())
    #判断行列的奇偶性，奇数为黑，偶数为白
    if r%2 == 1 and c%2 == 1:
        print('
