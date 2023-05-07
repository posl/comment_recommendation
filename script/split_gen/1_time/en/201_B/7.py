def main():
    N = int(input())
    mountain = {}
    for _ in range(N):
        s, t = input().split()
        mountain[s] = int(t)
    mountain = sorted(mountain.items(), key=lambda x: x[1], reverse=True)
    print(mountain[1][0])
