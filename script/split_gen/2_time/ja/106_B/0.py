def main():
    N = int(input())
    count = 0
    for i in range(1, N+1, 2):
        if len(divisors(i)) == 8:
            count += 1
    print(count)
