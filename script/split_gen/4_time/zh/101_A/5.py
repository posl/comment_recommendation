def main():
    S = input()
    sum = 0
    for i in range(0, 4):
        if S[i] == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)
