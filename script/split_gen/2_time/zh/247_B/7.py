def check_name(name_list):
    for i in range(len(name_list)):
        for j in range(i+1,len(name_list)):
            if name_list[i][0] == name_list[j][0] or name_list[i][0] == name_list[j][1] or name_list[i][1] == name_list[j][0] or name_list[i][1] == name_list[j][1]:
                return 'Yes'
    return 'No'
N = int(input())
name_list = []
for i in range(N):
    name = input().split(' ')
    name_list.append(name)
print(check_name(name_list))
