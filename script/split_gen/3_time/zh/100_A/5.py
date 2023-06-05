def main():
    #输入
    #A B
    #A和B是1到16（包括）之间的整数。
    #A+B最多为16。
    A,B=map(int,input().split())
    #如果E869120和square1001都能听从纸条上的指令，并取走所需数量的蛋糕，则打印Yay！；否则，打印:(。
    if A<=8 and B<=8:
        print("Yay!")
    else:
        print(":(")
