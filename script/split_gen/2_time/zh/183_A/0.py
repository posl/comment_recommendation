def relu(x):
    if x >= 0:
        return x
    else:
        return 0
x = int(input())
print(relu(x))
