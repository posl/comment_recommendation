def main():
    N = int(input())
    print(N%1000)
    if N%1000 == 0:
        print(0)
    else:
        print(1000 - N%1000)
