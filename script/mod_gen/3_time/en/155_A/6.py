def poor(a,b,c):
    if a == b and a != c:
        return 'Yes'
    elif b == c and b != a:
        return 'Yes'
    elif a == c and a != b:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    poor()