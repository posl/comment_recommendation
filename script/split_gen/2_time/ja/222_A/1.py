def main():
    N = int(input())
    if N < 10:
        print("000" + str(N))
    elif N < 100:
        print("00" + str(N))
    elif N < 1000:
        print("0" + str(N))
    else:
        print(N)
