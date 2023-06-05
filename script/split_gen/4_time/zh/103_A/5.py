def main():
    a1, a2, a3 = map(int, input().split())
    print(min(abs(a1-a2)+abs(a2-a3), abs(a1-a3)+abs(a3-a2), abs(a2-a1)+abs(a1-a3)))
