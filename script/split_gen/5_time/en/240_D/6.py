def main():
    N = int(input())
    a_list = [int(x) for x in input().split()]
    a_dict = {}
    for i in range(len(a_list)):
        if a_list[i] in a_dict:
            a_dict[a_list[i]] += 1
        else:
            a_dict[a_list[i]] = 1
    ans_list = []
    ans_list.append(len(a_dict))
    for i in range(1, len(a_list)):
        if a_list[i-1] in a_dict:
            a_dict[a_list[i-1]] -= 1
            if a_dict[a_list[i-1]] == 0:
                del a_dict[a_list[i-1]]
        ans_list.append(len(a_dict))
    for i in range(len(ans_list)):
        print(ans_list[i])
