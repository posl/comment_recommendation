def count(h,w,k):
    if w == 1:
        return 1
    if k == 1:
        return count(h,w-1,2)
    if k == w:
        return count(h,w-1,w-1)
    return count(h,w-1,k-1) + count(h,w-1,k+1)

if __name__ == '__main__':
    count()