def swap(a, b, li):
    tmp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = tmp

if __name__ == '__main__':
    swap()