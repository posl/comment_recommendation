def main():
    N = int(input())
    n = N//111
    if N%111 != 0:
        n += 1
    print(n*111)
