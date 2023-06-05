def problems279_a(S):
    # print(S)
    count = 0
    for i in range(len(S)):
        if S[i] == 'w':
            count += 1
    return count

if __name__ == '__main__':
    problems279_a()