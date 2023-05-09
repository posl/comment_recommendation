def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(2 * i - 2)
    else:
        if i * (i - 1) >= N:
            print(2 * i - 3)
        else:
            print(2 * i - 2)
