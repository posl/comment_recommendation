def main():
    n = int(input())
    if n < 10:
        print("000" + str(n))
    elif n < 100:
        print("00" + str(n))
    elif n < 1000:
        print("0" + str(n))
    else:
        print(n)
