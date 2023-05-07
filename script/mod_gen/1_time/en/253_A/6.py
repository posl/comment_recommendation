def check_median(a,b,c):
    if b in range(min(a,c),max(a,c)+1):
        return True
    else:
        return False

if __name__ == '__main__':
    check_median()