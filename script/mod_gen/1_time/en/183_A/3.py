def ReLU(x):
    if x<0:
        return 0
    else:
        return x
x = int(input())
print(ReLU(x))

if __name__ == '__main__':
    ReLU()