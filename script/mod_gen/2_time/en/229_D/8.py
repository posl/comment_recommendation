def problem():
    # input
    S = input()
    K = int(input())
    
    # initialization
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    
    # output
    print(max_count + K)

if __name__ == '__main__':
    problem()