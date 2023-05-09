def main():
    N = int(input())
    century = N // 100
    if N % 100 == 0:
        print(century)
    else:
        print(century + 1)
