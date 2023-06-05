def rotate90(input):
    result = []
    for i in range(len(input)):
        result.append([])
        for j in range(len(input)):
            result[i].append(input[j][i])
    return result
