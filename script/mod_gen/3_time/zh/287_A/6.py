def majority_vote(s_list):
    for i in range(len(s_list)):
        if s_list[i] == "For":
            s_list[i] = 1
        elif s_list[i] == "Against":
            s_list[i] = 0
    if sum(s_list) > len(s_list)/2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    majority_vote()