def tax(a,b):
    if a < 1 or a > 100 or a > b:
        return -1
    for i in range(1,100):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1
a,b = input().split()
a = int(a)
b = int(b)
print(tax(a,b))
