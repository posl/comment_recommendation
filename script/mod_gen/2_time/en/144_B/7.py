def is_multiple(x, y):
    return x * y
n = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if is_multiple(i, j) == n:
            print('Yes')
            exit()
print('No')

if __name__ == '__main__':
    is_multiple()