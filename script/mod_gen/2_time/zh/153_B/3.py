def judge(h,n,a):
    if h<=0:
        return True
    if n==0:
        return False
    if judge(h-a[0],n-1,a[1:]):
        return True
    if judge(h,n-1,a[1:]):
        return True
    return False

if __name__ == '__main__':
    judge()