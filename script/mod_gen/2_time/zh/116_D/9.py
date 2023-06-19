def solve():
    N,K = map(int,input().split())
    sushi = []
    for i in range(N):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])
    #print(sushi)
    eat = []
    eat_type = set()
    eat_type_num = 0
    eat_num = 0
    eat_type_num_max = 0
    eat_type_num_max_list = []
    eat_num_max = 0
    eat_num_max_list = []
    eat_num_max_list_2 = []
    for i in range(N):
        if sushi[i][0] not in eat_type:
            if eat_type_num == K:
                break
            eat.append(sushi[i])
            eat_type.add(sushi[i][0])
            eat_type_num += 1
            eat_num += sushi[i][1]
        else:
            eat_num_max_list.append(sushi[i])
    #print(eat_num_max_list)
    for i in range(len(eat_num_max_list)):
        if eat_num_max_list[i][1] not in eat_num_max_list_2:
            eat_num_max_list_2.append(eat_num_max_list[i][1])
    #print(eat_num_max_list_2)
    eat_num_max_list_2.sort(reverse=True)
    #print(eat_num_max_list_2)
    for i in range(len(eat_num_max_list_2)):
        for j in range(len(eat_num_max_list)):
            if eat_num_max_list_2[i] == eat_num_max_list[j][1]:
                eat_num_max_list_2[i] = eat_num_max_list[j]
    #print(eat_num_max_list_2)
    for i in range(len(eat_num_max_list_2)):
        if eat_num_max_list_2[i][0] not in eat_type:
            eat.append(eat_num_max_list_2[i])
            eat_type.add(eat_num_max_list_2[i][0])
            eat_num += eat_num_max_list_2[i][1]
            eat_type_num += 1
            break
    #print(eat)
    #print(eat_type)
    #print(eat_num)
    #print(eat_type_num)
    #print(eat_type_num_max_list)
    #print(eat

if __name__ == '__main__':
    solve()