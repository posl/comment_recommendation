def main():
    n = int(input())
    if n < 2 or n > 10:
        print('N must be 2 <= N <= 10')
        return
    total = 0
    for i in range(n):
        p = int(input())
        if p < 100 or p > 10000:
            print('p must be 100 <= p <= 10000')
            return
        if p % 2 != 0:
            print('p must be even number')
            return
        if p > 10000:
            print('p must be 100 <= p <= 10000')
            return
        total += p
    print(total - int(max(p)/2))
