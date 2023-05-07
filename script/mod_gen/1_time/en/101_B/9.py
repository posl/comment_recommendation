def SumOfDigits(n):
    return sum(int(c) for c in str(n))
n = int(input())

if __name__ == '__main__':
    SumOfDigits()