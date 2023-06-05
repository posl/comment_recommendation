def getMinSnack(A, B):
    if A < B:
        min = A
    else:
        min = B
    while True:
        if A % min == 0 and B % min == 0:
            break
        min -= 1
    return min
input = input().split()
A = int(input[0])
B = int(input[1])
min = getMinSnack(A, B)
print(A*B//min)

if __name__ == '__main__':
    getMinSnack()