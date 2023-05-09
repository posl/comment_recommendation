def function(x):
    if x == 0:
        return 1
    else:
        return x * function(x - 1)
print(function(int(input())))
