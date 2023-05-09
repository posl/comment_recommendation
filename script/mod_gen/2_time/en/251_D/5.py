def get_weight(w):
    if w==1:
        return 1
    if w==2:
        return 2
    if w==3:
        return 3
    if w==4:
        return 4
    if w==5:
        return 5
    if w==6:
        return 6
    if w%2==0:
        return 2
    if w%3==0:
        return 3
    if w%5==0:
        return 5
    return 1

if __name__ == '__main__':
    get_weight()