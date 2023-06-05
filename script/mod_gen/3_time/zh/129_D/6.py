def get_max_lighting_num(h, w, s):
    #print("h: {}, w: {}, s: {}".format(h, w, s))
    max_lighting_num = 0
    for i in range(h):
        lighting_num = 0
        for j in range(w):
            if s[i][j] == '#':
                lighting_num = 0
            else:
                lighting_num += 1
                max_lighting_num = max(max_lighting_num, lighting_num)
        #print("lighting_num: {}".format(lighting_num))
    #print("max_lighting_num: {}".format(max_lighting_num))
    for j in range(w):
        lighting_num = 0
        for i in range(h):
            if s[i][j] == '#':
                lighting_num = 0
            else:
                lighting_num += 1
                max_lighting_num = max(max_lighting_num, lighting_num)
        #print("lighting_num: {}".format(lighting_num))
    #print("max_lighting_num: {}".format(max_lighting_num))
    return max_lighting_num - 1

if __name__ == '__main__':
    get_max_lighting_num()