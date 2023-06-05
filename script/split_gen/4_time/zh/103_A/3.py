def main():
    a1,a2,a3 = map(int, input().split())
    print(abs(a1-a2)+abs(a2-a3)+abs(a3-a1)-max(abs(a1-a2),abs(a2-a3),abs(a3-a1)))
