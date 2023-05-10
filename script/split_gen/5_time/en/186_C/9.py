def main():
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        answer += 1
    print(answer)
