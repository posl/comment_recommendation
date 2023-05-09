def main():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append([s, int(p), i+1])
    data.sort(key=lambda x:(x[0],-x[1]))
    for i in range(n):
        print(data[i][2])
