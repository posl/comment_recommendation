def getAllowance(a, b, c):
    result = 0
    if a < b:
        temp = a
        a = b
        b = temp
    if a < c:
        temp = a
        a = c
        c = temp
    if b < c:
        temp = b
        b = c
        c = temp
    result = a * 10 + b + c
    return result
a, b, c = map(int, input().split())
print(getAllowance(a, b, c))

if __name__ == '__main__':
    getAllowance()