def main():
    N = int(input())
    print(N%1000)
    if N%1000 != 0:
        print(1000 - N%1000)
    else:
        print(0)
