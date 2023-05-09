def main():
    S = input()
    pin_list = list(S)
    pin_list = [int(s) for s in pin_list]
    #print(pin_list)
    #print(pin_list[0])
    #print(pin_list[1])
    #print(pin_list[2])
    #print(pin_list[3])
    #print(pin_list[4])
    #print(pin_list[5])
    #print(pin_list[6])
    #print(pin_list[7])
    #print(pin_list[8])
    #print(pin_list[9])
    #print(pin_list[10])
    if pin_list[0] == 0:
        print('Yes')
    elif pin_list[1] == 0 and pin_list[5] == 0:
        print('Yes')
    elif pin_list[2] == 0 and pin_list[6] == 0:
        print('Yes')
    elif pin_list[3] == 0 and pin_list[7] == 0:
        print('Yes')
    elif pin_list[4] == 0 and pin_list[8] == 0:
        print('Yes')
    elif pin_list[5] == 0 and pin_list[9] == 0:
        print('Yes')
    else:
        print('No')
