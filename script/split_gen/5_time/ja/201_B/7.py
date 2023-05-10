def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        mountains.append([s, t])
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])
