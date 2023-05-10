def main():
    # input
    S = input()
    # solve
    count = 0
    max = 0
    for i in S:
        if i == 'R':
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    # output
    print(max)
