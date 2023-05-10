def main():
    N = int(input())
    prime_list = []
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            prime_list.append(i)
            while N % i == 0:
                N //= i
    if N != 1:
        prime_list.append(N)
    print(len(set(prime_list)))
