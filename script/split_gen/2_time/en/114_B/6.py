def main():
    s = input()
    s = [int(i) for i in s]
    answer = 753
    for i in range(len(s)-2):
        if answer > abs(753 - int(s[i] * 100 + s[i+1] * 10 + s[i+2])):
            answer = abs(753 - int(s[i] * 100 + s[i+1] * 10 + s[i+2]))
    print(answer)
