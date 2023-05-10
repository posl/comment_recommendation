def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print("Yes" if S.count("For") > N/2 else "No")
