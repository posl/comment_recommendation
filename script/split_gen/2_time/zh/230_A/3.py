def main():
    n = int(input())
    if n <= 9:
        print("AGC00" + str(n))
    elif n <= 99:
        print("AGC0" + str(n))
    else:
        print("AGC" + str(n))
