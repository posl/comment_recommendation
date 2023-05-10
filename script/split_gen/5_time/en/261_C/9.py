def main():
    N = int(input())
    file_list = []
    for i in range(N):
        file_list.append(input())
    
    file_dict = {}
    for file_name in file_list:
        if file_name in file_dict:
            file_dict[file_name] += 1
        else:
            file_dict[file_name] = 0
        print(file_name + '(' + str(file_dict[file_name]) + ')') if file_dict[file_name] > 0 else print(file_name)
