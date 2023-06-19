def main():
    #print("请输入五个整数：")
    num = input()
    num_list = num.split()
    num_set = set(num_list)
    print(len(num_set))
