def solve(a, b):
    if (a == 8 and b == 13) or (a == 13 and b == 8):
        return 'Yes'
    elif (a == 1 and b == 15) or (a == 15 and b == 1):
        return 'Yes'
    elif (a == 4 and b == 12) or (a == 12 and b == 4):
        return 'Yes'
    elif (a == 5 and b == 9) or (a == 9 and b == 5):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    solve()