def check753(num):
    num = str(num)
    if num.count("7") > 0 and num.count("5") > 0 and num.count("3") > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    check753()