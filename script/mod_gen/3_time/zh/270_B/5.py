def problem270_b(x,y,z):
    if z>y:
        return -1
    return x+y+z
print(problem270_b(10,-10,1))
print(problem270_b(20,10,-10))
print(problem270_b(100,1,1000))
