def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountain = input().split()
        mountains.append(mountain)
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])
