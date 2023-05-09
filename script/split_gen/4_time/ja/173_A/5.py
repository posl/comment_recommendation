def main():
    N = int(input())
    if N < 1000:
        print(1000 - N)
    else:
        print(N % 1000)
