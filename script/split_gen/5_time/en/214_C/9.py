def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    #print(n, s_list, t_list)
    s_list2 = s_list.copy()
    t_list2 = t_list.copy()
    for i in range(n):
        s_list2[i] = [s_list[i], i]
        t_list2[i] = [t_list[i], i]
    #print(s_list2, t_list2)
    s_list2.sort()
    t_list2.sort()
    #print(s_list2, t_list2)
    s_list3 = s_list2.copy()
    t_list3 = t_list2.copy()
    for i in range(n):
        if i == 0:
            s_list3[i][0] = 0
        else:
            s_list3[i][0] = s_list2[i][0] - s_list2[i-1][0]
        if i == 0:
            t_list3[i][0] = 0
        else:
            t_list3[i][0] = t_list2[i][0] - t_list2[i-1][0]
    #print(s_list3, t_list3)
    s_list3.sort(key=lambda x: x[1])
    t_list3.sort(key=lambda x: x[1])
    #print(s_list3, t_list3)
    ans_list = [0]*n
    for i in range(n):
        ans_list[t_list3[i][1]] = ans_list[s_list3[i][1]] + s_list3[i][0]
    #print(ans_list)
    for i in range(n):
        print(ans_list[i])
