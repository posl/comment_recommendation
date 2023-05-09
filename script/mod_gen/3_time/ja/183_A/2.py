def relu(x):
    if x < 0:
        return 0
    else:
        return x
x = int(input())
print(relu(x))

if __name__ == '__main__':
    relu()