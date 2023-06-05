def check_on_off(switch, bulb, p):
    #print("switch: ", switch)
    #print("bulb: ", bulb)
    #print("p: ", p)
    for i in range(bulb):
        count = 0
        for j in range(len(switch[i])):
            if switch[i][j] in p:
                count += 1
        if count % 2 != p[i]:
            return False
    return True
