def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input()
        names.append(name)
    print(sorted(names)[n//2])
