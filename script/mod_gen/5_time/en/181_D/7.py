def solve(digit):
    if len(digit) == 1:
        if digit[0] == "8":
            return True
        else:
            return False
    elif len(digit) == 2:
        if int(digit[0]+digit[1])%8 == 0 or int(digit[1]+digit[0])%8 == 0:
            return True
        else:
            return False
    else:
        digit_count = [0] * 10
        for i in range(len(digit)):
            digit_count[int(digit[i])] += 1
        for i in range(104,1000,8):
            if i%8 == 0:
                tmp = i
                tmp_count = [0] * 10
                while tmp > 0:
                    tmp_count[tmp%10] += 1
                    tmp //= 10
                flag = True
                for j in range(10):
                    if tmp_count[j] > digit_count[j]:
                        flag = False
                if flag:
                    return True
        return False

if __name__ == '__main__':
    solve()