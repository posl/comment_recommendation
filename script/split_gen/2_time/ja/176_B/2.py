def main():
    N = input()
    N = int(N)
    sum = 0
    while N > 0:
        sum += N % 10
        N = N // 10
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")
