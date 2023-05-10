def rotate90(list):
    result = []
    for i in range(len(list[0])):
        tmp = []
        for j in range(len(list)):
            tmp.append(list[j][i])
        tmp.reverse()
        result.append(tmp)
    return result

if __name__ == '__main__':
    rotate90()