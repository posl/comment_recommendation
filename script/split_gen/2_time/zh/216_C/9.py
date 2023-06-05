def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    if len(names) == len(set(names)):
        print("No")
    else:
        print("Yes")
