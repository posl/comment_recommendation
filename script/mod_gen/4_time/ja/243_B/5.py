def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_index = {}
    b_index = {}
    for i in range(n):
        a_index[a[i]] = i
        b_index[b[i]] = i
    a_and_b = 0
    a_and_b_not_same_index = 0
    for i in range(1, n+1):
        if a_index[i] == b_index[i]:
            a_and_b += 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if a_index[i] == b_index[j]:
                    a_and_b_not_same_index += 1
    print(a_and_b)
    print(a_and_b_not_same_index)

if __name__ == '__main__':
    main()