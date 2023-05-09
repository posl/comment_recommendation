def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {a: i for i, a in enumerate(A)}
    B_dict = {b: i for i, b in enumerate(B)}
    A_B_dict = {a: B_dict[a] for a in A_dict.keys() & B_dict.keys()}
    A_B_list = list(A_B_dict.items())
    A_B_list.sort(key=lambda x: x[1])
    A_B_list = [a for a, b in A_B_list]
    A_B_list = [a for a in A_B_list if A_dict[a] == B_dict[a]]
    print(len(A_B_list))
    print(len(A_B_dict) - len(A_B_list))
