def main():
    N = int(input())
    z = 2
    count = 0
    while N != 1:
        if N % z == 0:
            N = N // z
            count += 1
        else:
            z += 1
    print(count)
