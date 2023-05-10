def main():
    n = int(input())
    answer = 0
    for i in range(1, n):
        for j in range(1, n):
            if i*j < n:
                answer += 1
            else:
                break
    print(answer)
