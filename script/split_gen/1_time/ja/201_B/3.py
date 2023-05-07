def main():
    n = int(input())
    mountain = []
    for i in range(n):
        s, t = input().split()
        mountain.append([s, int(t)])
    mountain.sort(key=lambda x: x[1], reverse=True)
    print(mountain[1][0])
