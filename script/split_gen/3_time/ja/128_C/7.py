def checkLight(switch, light):
    for i in range(len(light)):
        count = 0
        for j in range(1, len(light[i])):
            if switch[light[i][j] - 1] == 1:
                count += 1
        if count % 2 != light[i][0]:
            return False
    return True
