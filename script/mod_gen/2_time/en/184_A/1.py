def determinant(a, b, c, d):
    return a * d - b * c
a, b = map(int, input().split())
c, d = map(int, input().split())
print(determinant(a, b, c, d))

if __name__ == '__main__':
    determinant()