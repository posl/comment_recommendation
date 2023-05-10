def main():
    v,t,s,d = map(int, input().split())
    if d/(v*t) <= s and d/(v*t) >= t:
        print("No")
    else:
        print("Yes")
