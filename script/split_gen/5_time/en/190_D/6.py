def main():
    N = int(input())
    result = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            if N // i - i > 0 and (N // i - i) % 2 == 1:
                result += 1
            if i - 1 > 0 and (i - 1) % 2 == 1:
                result += 1
    print(result)
