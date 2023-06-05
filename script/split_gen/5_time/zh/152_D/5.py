def find_ab(x):
    count = 0
    for i in range(1,x+1):
        for j in range(1,x+1):
            a = str(i)
            b = str(j)
            if a[-1] == b[0] and a[0] == b[-1]:
                count += 1
    return count
x = int(input())
print(find_ab(x))
