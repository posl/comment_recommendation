def main():
    N = int(input())
    k = 0
    while N > 1:
        N /= 2
        k += 1
    print(k)
