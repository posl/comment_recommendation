def main():
    L,Q = map(int,input().split())
    cut_list = []
    for i in range(Q):
        cut_list.append(list(map(int,input().split())))
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,L])
    #print(cut_list)
    cut_num = 0
    cut_left = 0
    cut_right = L
    for i in range(1,Q+1):
        if cut_list[i][0] == 1:
            if cut_list[i][1] < cut_left:
                cut_num += 0
            elif cut_list[i][1] > cut_right:
                cut_num += 0
            else:
                cut_num += 1
                cut_right = cut_list[i][1]
                cut_left = cut_list[i][1]
        elif cut_list[i][0] == 2:
            print(cut_right-cut_left)
        else:
            print("error")
        #print(cut_num,cut_left,cut_right)

if __name__ == '__main__':
    main()