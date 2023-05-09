def main():
    N = int(input())
    A = [input() for _ in range(N)]
    print("Yes" if A.count("For") > N // 2 else "No")
