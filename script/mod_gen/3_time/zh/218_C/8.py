def rotate_90(li):
    li_new = []
    for i in range(len(li)):
        li_new.append([])
        for j in range(len(li)):
            li_new[i].append(li[len(li)-1-j][i])
    return li_new

if __name__ == '__main__':
    rotate_90()