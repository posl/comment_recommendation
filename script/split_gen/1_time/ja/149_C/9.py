def main():
    X = int(input())
    for i in range(X, 100001):
        if is_prime(i):
            print(i)
            break
