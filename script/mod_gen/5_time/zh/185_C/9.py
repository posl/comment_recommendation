def cutbar(m,n,current):
    if current >= n:
        return 0
    elif current < m:
        return 1 + cutbar(m,n,current*2)
    else:
        return 1 + cutbar(m,n,current+m)
print(cutbar(3,20,1))
print(cutbar(5,100,1))
print(cutbar(12,200,1))
