def main():
    # input
    S = input()
    # process
    answer = 0
    for s in S:
        if s == '+':
            answer += 1
        else:
            answer -= 1
    # output
    print(answer)
