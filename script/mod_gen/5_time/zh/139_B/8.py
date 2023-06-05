def cal(a,b):
    if a == 1:
        return 0
    if b <= a:
        return 1
    if b % a == 0:
        return int(b/a)
    else:
        return int(b/a)+1

if __name__ == '__main__':
    cal()