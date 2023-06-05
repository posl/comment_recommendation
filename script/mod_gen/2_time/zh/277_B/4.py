def get_input():
    input1 = input("请输入两个数，以空格分开：")
    input2 = input("请输入一个数，以空格分开：")
    input1 = input1.split(" ")
    input2 = input2.split(" ")
    # print(input1)
    # print(input2)
    return input1, input2

if __name__ == '__main__':
    get_input()