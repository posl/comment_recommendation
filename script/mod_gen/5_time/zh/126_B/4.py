def checkMonth(month):
    if month < 1 or month > 12:
        return False
    return True

if __name__ == '__main__':
    checkMonth()