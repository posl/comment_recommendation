def main():
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        answer += i - 1
    print(answer)
