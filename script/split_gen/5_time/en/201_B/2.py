def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append((S, T))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])
