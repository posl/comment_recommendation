def getNthMinNumDivisibleBy100(D,N):
    #D是0，1或2。N是1到100（包括）之间的整数。
    #能被100整除D次的整数如下：
    #D=0 1, 2, 3, 4, 5, 6, 7, ...
    #D=1 100, 200, 300, 400, 500, 600, 700, 800, 900, 1 000, 1 100, ...
    #D=2 10 000, 20 000, 30 000, ...
    if D==0:
        return N
    elif D==1:
        return N*100
    elif D==2:
        return N*10000

if __name__ == '__main__':
    getNthMinNumDivisibleBy100()