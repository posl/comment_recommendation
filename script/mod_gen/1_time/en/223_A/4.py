def purse(x):
    if x % 100 == 0 and x != 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    purse()