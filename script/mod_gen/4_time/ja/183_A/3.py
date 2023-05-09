def relu(x):
    if x < 0:
        return 0
    else:
        return x
print(relu(int(input())))

if __name__ == '__main__':
    relu()