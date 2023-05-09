def det(a, b, c, d):
    return (a * d) - (b * c)
a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
print(det(a, b, c, d))

if __name__ == '__main__':
    det()