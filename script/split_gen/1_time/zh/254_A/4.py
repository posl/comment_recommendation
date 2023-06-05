def last_two_digits(N):
    if N < 100 or N > 999:
        print("N is not in the range of 100 to 999.")
    else:
        print(N%100)
N = int(input())
last_two_digits(N)
