def main():
    N = int(input())
    if N >= -2 ** 31 and N <= 2 ** 31 - 1:
        print("是")
    else:
        print("否")
