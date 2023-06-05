def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input())
    data.sort()
    for i in range(n-1):
        if data[i] == data[i+1]:
            print("Yes")
            break
    else:
        print("No")
