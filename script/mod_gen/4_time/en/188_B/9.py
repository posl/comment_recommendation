def inner_product(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i] * b[i]
    return result
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print("Yes" if inner_product(a, b) == 0 else "No")

if __name__ == '__main__':
    inner_product()