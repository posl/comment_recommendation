def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i * i != N:
                print(N // i)
        i += 1
