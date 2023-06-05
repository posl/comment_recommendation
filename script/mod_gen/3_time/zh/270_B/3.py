def problems270_b(x,y,z):
    if x > 0 and y > 0 and z > 0:
        return -1
    elif x < 0 and y < 0 and z < 0:
        return -1
    elif x > 0 and y < 0 and z < 0:
        return -1
    elif x < 0 and y > 0 and z > 0:
        return -1
    elif x > 0 and y > 0 and z < 0:
        return -1
    elif x > 0 and y < 0 and z > 0:
        return -1
    elif x < 0 and y > 0 and z < 0:
        return -1
    elif x < 0 and y < 0 and z > 0:
        return -1
    else:
        return abs(x - y) + abs(y - z)
print(problems270_b(10,-10,1))
print(problems270_b(20,10,-10))
print(problems270_b(100,1,1000))
