def main():
    N = int(input())
    print("Yes" if N % sum(int(i) for i in str(N)) == 0 else "No")
