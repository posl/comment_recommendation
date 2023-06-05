def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if len(set(s)) == n:
        print("Yes")
    else:
        print("No")
