def main():
    S = input()
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)
