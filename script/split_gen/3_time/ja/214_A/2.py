def main():
    N = int(input())
    if N <= 125:
        print(4)
    elif 126 <= N <= 211:
        print(6)
    else:
        print(8)
