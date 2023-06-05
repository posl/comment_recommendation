def check_line(line):
    if line.count('#') >= 6:
        return True
    else:
        return False

if __name__ == '__main__':
    check_line()