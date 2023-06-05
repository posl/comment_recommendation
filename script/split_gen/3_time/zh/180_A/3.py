def main():
    print("请输入N A B:")
    str = input()
    str_list = str.split(" ")
    N = int(str_list[0])
    A = int(str_list[1])
    B = int(str_list[2])
    print(N + B - A)
