def main():
    V, T, S, D = map(int, input().split())
    print("Yes" if D < V*T or V*S < D else "No")
