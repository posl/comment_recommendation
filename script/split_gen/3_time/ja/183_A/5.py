def relu(x):
    if x < 0:
        x = 0
    return x
x = int(input())
print(relu(x))
