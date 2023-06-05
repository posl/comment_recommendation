def main():
    N,M = map(int,input().split())
    #print(N,M)
    input_list = []
    for i in range(M):
        input_list.append(list(map(int,input().split())))
    #print(input_list)
    input_list = sorted(input_list,key=lambda x:x[1])
    #print(input_list)
    input_dict = {}
    for i in range(M):
        if input_list[i][0] not in input_dict:
            input_dict[input_list[i][0]] = 1
        else:
            input_dict[input_list[i][0]] += 1
    #print(input_dict)
    input_dict2 = {}
    for i in range(M):
        if input_list[i][0] not in input_dict2:
            input_dict2[input_list[i][0]] = 1
        else:
            input_dict2[input_list[i][0]] += 1
        input_list[i].append(input_dict2[input_list[i][0]])
    #print(input_list)
    input_list = sorted(input_list,key=lambda x:x[0])
    #print(input_list)
    for i in range(M):
        print(str(input_list[i][0]).zfill(6)+str(input_list[i][3]).zfill(6))
