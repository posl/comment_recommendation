def main():
    name_list = []
    flag = False
    for i in range(int(input())):
        name = input()
        if name in name_list:
            flag = True
            break
        name_list.append(name)
    if flag:
        print('Yes')
    else:
        print('No')
