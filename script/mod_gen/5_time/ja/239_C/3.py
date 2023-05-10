def solve(x1,y1,x2,y2):
    if abs(x1-x2) == 5**0.5 and abs(y1-y2) == 5**0.5:
        return 'Yes'
    elif abs(x1-y2) == 5**0.5 and abs(y1-x2) == 5**0.5:
        return 'Yes'
    elif abs(x1-x2) == 5**0.5 and abs(y1-y2) == 5**0.5:
        return 'Yes'
    elif abs(x1-y2) == 5**0.5 and abs(y1-x2) == 5**0.5:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    solve()