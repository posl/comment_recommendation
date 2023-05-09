def main():
    pins = input()
    if pins[0] == '0':
        if pins[1] == '0' or pins[5] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[9] == '0':
        if pins[8] == '0' or pins[4] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[1] == '0':
        if pins[2] == '0' or pins[6] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[8] == '0':
        if pins[7] == '0' or pins[3] == '0':
            print('No')
        else:
            print('Yes')
    else:
        print('No')
