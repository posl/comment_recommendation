def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    if max_count < K:
        max_count = K
    print(max_count)
main()
