def is_split(pin):
    if pin[0] == '0':
        return False
    for i in range(1, 10):
        if pin[i-1] == '1' and pin[i] == '0':
            for j in range(i+1, 10):
                if pin[j] == '1':
                    return True
    return False

if __name__ == '__main__':
    is_split()