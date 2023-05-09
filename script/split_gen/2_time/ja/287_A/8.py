def main():
    N = int(input())
    s = [input() for _ in range(N)]
    print("Yes" if s.count("For") > N//2 else "No")
