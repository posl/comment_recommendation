def main():
    A, B, W = map(int, input().split())
    min = 0
    max = 0
    if W * 1000 % B == 0:
        max = W * 1000 // B
    else:
        max = W * 1000 // B + 1
    if W * 1000 % A == 0:
        min = W * 1000 // A
    else:
        min = W * 1000 // A + 1
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)
