def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountain = input().split()
        mountain[1] = int(mountain[1])
        mountains.append(mountain)
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])
