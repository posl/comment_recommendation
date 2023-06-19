def is_8(x):
    x = str(x)
    if len(x) == 1:
        if x == '8':
            return True
        else:
            return False
    elif len(x) == 2:
        if int(x) % 8 == 0:
            return True
        elif int(x[1] + x[0]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(len(x)):
            for j in range(len(x)):
                for k in range(len(x)):
                    if i != j and j != k and k != i:
                        if int(x[i] + x[j] + x[k]) % 8 == 0:
                            return True
        return False
s = input()

if __name__ == '__main__':
    is_8()