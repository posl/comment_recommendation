def checkLine(line):
    if line.find("######")>=0:
        return True
    else:
        return False

if __name__ == '__main__':
    checkLine()