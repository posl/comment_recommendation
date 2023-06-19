def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    name.sort()
    for i in range(n-1):
        if name[i] == name[i+1]:
            print("Yes")
            break
    else:
        print("No")
