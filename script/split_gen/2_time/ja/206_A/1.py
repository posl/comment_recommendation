def main():
    N = int(input())
    if N < int(N * 1.08):
        print("Yay!")
    elif N == int(N * 1.08):
        print("so-so")
    else:
        print(":(")
