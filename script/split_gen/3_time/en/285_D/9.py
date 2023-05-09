def check(data):
    for i in range(len(data)-1):
        if data[i][1] == data[i+1][0]:
            return False
    return True
