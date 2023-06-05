def main():
    n = int(input())
    file_list = []
    for i in range(n):
        file_list.append(input())
    file_dict = {}
    for i in range(n):
        if file_list[i] not in file_dict:
            file_dict[file_list[i]] = 1
            print(file_list[i])
        else:
            file_dict[file_list[i]] += 1
            print(file_list[i] + '(' + str(file_dict[file_list[i]] - 1) + ')')
