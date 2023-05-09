def relu(x):
    if x >= 0:
        return x
    else:
        return 0
print(relu(int(input())))

if __name__ == '__main__':
    relu()