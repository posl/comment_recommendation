def odd_digits(N):
    return N - (N // 10)
N = int(input())
print(odd_digits(N))

if __name__ == '__main__':
    odd_digits()