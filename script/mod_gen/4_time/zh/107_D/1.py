def median(l):
    l.sort()
    return l[(len(l)-1)/2]

if __name__ == '__main__':
    median()