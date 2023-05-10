def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    result = 0
    for i in range(N):
        result += AB[i][0]
    result = result - result/2
    print(int(result))
