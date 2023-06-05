def main():
    v,t,s,d = map(int,input().split())
    print("Yes" if not (d < v * t or d > v * s) else "No")
