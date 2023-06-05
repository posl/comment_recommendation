def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    names.sort()
    for i in range(n-1):
        if names[i] == names[i+1]:
            print("Yes")
            break
    else:
        print("No")
