def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}
    a_b = set(a_dict.keys()) & set(b_dict.keys())
    a_b_same = set([i for i in a_dict.keys() if i in b_dict.keys() and a_dict[i] == b_dict[i]])
    a_b_diff = a_b - a_b_same
    print(len(a_b_same))
    print(len(a_b_diff))

if __name__ == '__main__':
    main()