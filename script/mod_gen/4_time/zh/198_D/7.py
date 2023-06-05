def get_int(str):
    return reduce(lambda x,y:10*x+y, map(lambda x:ord(x)-ord('a'), str))

if __name__ == '__main__':
    get_int()