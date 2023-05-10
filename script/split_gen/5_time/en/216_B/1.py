def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(set(names)) == n:
        print("No")
    else:
        print("Yes")
