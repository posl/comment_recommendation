def main():
    N = int(input())
    if N == 1:
        print("Hello World")
    elif N == 2:
        A, B = map(int, input().split())
        print(A+B)
    else:
        print("error")
