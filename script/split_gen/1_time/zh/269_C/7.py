def main():
    N = int(input())
    n = bin(N).count("1")
    for i in range(2 ** n):
        if bin(i).count("1") == n:
            print(i)
