def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    if len(A) == len(A_set):
        print(0)
        return
    A_dict = {}
    for a in A:
        if a in A_dict:
            A_dict[a] += 1
        else:
            A_dict[a] = 1
    A_dict = sorted(A_dict.items(), key=lambda x:x[1], reverse=True)
    print(N - A_dict[0][1])
