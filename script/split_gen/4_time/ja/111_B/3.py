def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            break
        else:
            N += 1
