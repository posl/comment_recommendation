def main():
    # input
    A, B, K = map(int, input().split())
    # compute
    divisors = []
    for i in range(1, min(A, B)+1):
        if A%i==0 and B%i==0:
            divisors.append(i)
    # output
    print(divisors[-K])
