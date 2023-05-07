def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i] == name[j]:
                print("Yes")
                return
    print("No")
