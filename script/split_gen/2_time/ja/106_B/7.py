def main():
    N = int(input())
    count = 0
    for i in range(1, N+1, 2):
        if i == 1:
            continue
        if len(list(divisor(i))) == 8:
            count += 1
    print(count)
