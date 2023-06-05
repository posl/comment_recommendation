def main():
    N = int(input())
    print(N + (111 - N % 111) if N % 111 != 0 else N)
