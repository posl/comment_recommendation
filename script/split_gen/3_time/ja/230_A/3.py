def main():
    N = int(input())
    if N <= 54:
        print("AGC" + str(N+1).zfill(3))
    else:
        print("AGC055")
