def check_light(lights, switches, p):
    for i in range(len(lights)):
        count = 0
        for j in range(1, len(switches[i])):
            if lights[switches[i][j]-1] == 1:
                count += 1
        if count % 2 != p[i]:
            return False
    return True

if __name__ == '__main__':
    check_light()