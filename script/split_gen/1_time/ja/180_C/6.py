def main():
    N = int(input())
    divisors = []
    i = 1
    while i*i <= N:
        if N%i == 0:
            divisors.append(i)
            if i*i != N:
                divisors.append(N//i)
        i += 1
    divisors.sort()
    for d in divisors:
        print(d)
