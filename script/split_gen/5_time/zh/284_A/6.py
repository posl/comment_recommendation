def main():
    num = int(input())
    str_list = []
    for i in range(num):
        str_list.append(input())
    for i in range(num):
        print(str_list[num-i-1])
