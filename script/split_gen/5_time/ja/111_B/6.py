def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N//111)*111+111)
