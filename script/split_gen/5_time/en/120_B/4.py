def main():
    A, B, K = map(int, input().split())
    divisors = []
    for i in range(1, min(A,B)+1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    print(divisors[-K])
