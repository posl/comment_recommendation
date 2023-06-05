def checkSplit(pins):
    #print(pins)
    #print(pins.count("1"))
    if pins.count("1") == 1:
        return False
    for i in range(1, 9):
        if pins[i] == "0":
            continue
        if pins[i-1] == "1" and pins[i+1] == "1":
            return True
    return False

if __name__ == '__main__':
    checkSplit()