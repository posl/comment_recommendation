def replace_num(n):
    n = str(n)
    n = n.replace("1","a")
    n = n.replace("9","1")
    n = n.replace("a","9")
    return n

if __name__ == '__main__':
    replace_num()