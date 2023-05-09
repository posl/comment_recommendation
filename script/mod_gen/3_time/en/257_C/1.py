def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    child = []
    adult = []
    for i in range(N):
        if S[i] == "0":
            child.append(W[i])
        else:
            adult.append(W[i])
    child.sort()
    adult.sort()
    child_sum = sum(child)
    adult_sum = sum(adult)
    child_acc = [0]
    adult_acc = [0]
    for i in range(len(child)):
        child_acc.append(child_acc[-1] + child[i])
    for i in range(len(adult)):
        adult_acc.append(adult_acc[-1] + adult[i])
    max_count = 0
    for i in range(len(child_acc)):
        adult_count = 0
        for j in range(len(adult_acc)):
            if child_acc[i] + adult_acc[j] <= adult_sum:
                adult_count = j
            else:
                break
        max_count = max(max_count, i + adult_count)
    print(max_count)

if __name__ == '__main__':
    main()