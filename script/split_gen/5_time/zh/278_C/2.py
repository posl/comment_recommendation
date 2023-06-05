def main():
    N, Q = map(int, input().split())
    follow = []
    for i in range(Q):
        follow.append(list(map(int, input().split())))
    follow.reverse()
    #print(follow)
    follow_list = []
    for i in range(Q):
        if follow[i][0] == 1:
            follow_list.append([follow[i][1], follow[i][2]])
        elif follow[i][0] == 2:
            follow_list.remove([follow[i][1], follow[i][2]])
        else:
            if [follow[i][1], follow[i][2]] in follow_list and [follow[i][2], follow[i][1]] in follow_list:
                print("Yes")
            else:
                print("No")
