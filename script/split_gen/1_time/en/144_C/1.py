def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(i + i - 2)
    else:
        if N % i == 0:
            print(i + i - 1)
        else:
            print(i + i - 2)
