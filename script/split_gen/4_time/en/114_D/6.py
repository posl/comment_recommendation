def main():
    N = int(input())
    divisors = [1]
    for i in range(2, N+1):
        divisors = [x*i for x in divisors]
        divisors = list(set(divisors))
    print(len([x for x in divisors if x % 75 == 0]))
