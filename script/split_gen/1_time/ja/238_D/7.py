def main():
    T = int(input())
    for _ in range(T):
        a,s = map(int,input().split())
        print("Yes" if a <= s and (s-a)%2 == 0 else "No")
