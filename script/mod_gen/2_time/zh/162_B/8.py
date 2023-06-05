def isSevenInNum(num):
    if num%10==7:
        return True
    elif num/10%10==7:
        return True
    elif num/100%10==7:
        return True
    else:
        return False
num = int(raw_input())

if __name__ == '__main__':
    isSevenInNum()