def ReLU(x):
    if x > 0:
        return x
    else:
        return 0
x = int(input())
print(ReLU(x))

if __name__ == '__main__':
    ReLU()