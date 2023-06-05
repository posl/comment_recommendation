def main():
    v,t,s,d = map(int, input().split())
    print("Yes" if d/v < t or d/v > s else "No")
