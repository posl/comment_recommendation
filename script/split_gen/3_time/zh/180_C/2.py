def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if N // i != i:
                print(N // i)
        i += 1
