def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if len(s) != len(set(s)):
        print("Yes")
    else:
        print("No")
