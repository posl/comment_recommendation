def main():
    N = int(input())
    names = set()
    for i in range(N):
        name = input()
        if name in names:
            print("Yes")
            return
        else:
            names.add(name)
    print("No")
    return
