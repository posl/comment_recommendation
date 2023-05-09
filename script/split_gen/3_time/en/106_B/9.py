def main():
    N = int(input())
    if N < 105:
        print("0")
    elif N == 105:
        print("1")
    else:
        print(N-105)
