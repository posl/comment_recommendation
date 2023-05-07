def prime_list(n):
    prime = [2]
    for i in range(3, n + 1, 2):
        for p in prime:
            if i % p == 0:
                break
        else:
            prime.append(i)
    return prime

if __name__ == '__main__':
    prime_list()