def main():
    S = input()
    sum = 0
    if S[0] == '+':
        sum += 1
    elif S[0] == '-':
        sum -= 1
    if S[1] == '+':
        sum += 1
    elif S[1] == '-':
        sum -= 1
    if S[2] == '+':
        sum += 1
    elif S[2] == '-':
        sum -= 1
    if S[3] == '+':
        sum += 1
    elif S[3] == '-':
        sum -= 1
    print(sum)
