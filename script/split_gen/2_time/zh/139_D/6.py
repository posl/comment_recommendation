def main():
    N = int(input())
    i = 1
    sum = 0
    while i <= N:
        sum += N % i
        i += 1
    print(sum)
