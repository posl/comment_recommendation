def isLight(s, t, x):
    if s < t:
        return s <= x and x < t
    elif s > t:
        return s <= x or x < t
    else:
        return False
s, t, x = map(int, input().split())

if __name__ == '__main__':
    isLight()