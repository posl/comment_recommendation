def main():
    #读取数据
    input_str = input()
    input_list = input_str.split()
    N = int(input_list[0])
    a = int(input_list[1])
    b = int(input_list[2])
    #计算答案
    #先计算A的倍数之和
    sum_a = 0
    if a <= N:
        sum_a = a*(N//a)*(N//a+1)//2
    #再计算B的倍数之和
    sum_b = 0
    if b <= N:
        sum_b = b*(N//b)*(N//b+1)//2
    #再计算A和B的最小公倍数的倍数之和
    sum_ab = 0
    if a*b <= N:
        sum_ab = a*b*(N//(a*b))*(N//(a*b)+1)//2
    #最后减去A和B的最小公倍数的倍数之和
    sum_ans = sum_a + sum_b - sum_ab
    #输出答案
    print(sum_ans)

if __name__ == '__main__':
    main()