def find_zero():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            return i + 1
print(find_zero())
