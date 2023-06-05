def main():
    N = int(input())
    if N < 16:
        print("0" + hex(N)[2:])
    else:
        print(hex(N)[2:])
