def main():
    #输入
    N = int(input())
    S = list(map(int,input().split()))
    #计算
    count = 0
    for i in range(N):
        # 4ab+3a+3b = S_i
        # 4ab+3a+3b-S_i = 0
        # (4b+3)a+(4a+3)b-S_i = 0
        # (4b+3)a = (S_i-(4a+3)b)
        # a = (S_i-(4a+3)b)/(4b+3)
        # b = (S_i-(4b+3)a)/(4a+3)
        # a = (S_i-(4a+3)((S_i-(4b+3)a)/(4a+3)))/(4((S_i-(4b+3)a)/(4a+3))+3)
        # a = (S_i-(4a+3)((S_i-(4b+3)a)/(4a+3)))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
        # a = (S_i-(4a+3)(S_i-(4b+3)a)/(4a+3))/(S_i-(4b+3)a+3)
