def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    mod_dict = {}
    for i, a in enumerate(A):
        mod_a = a % mod
        if mod_a in mod_dict:
            print("Yes")
            print(i + 1, *mod_dict[mod_a])
            print(i + 1, *[j + 1 for j in range(N) if j not in mod_dict[mod_a]])
            return
        else:
            mod_dict[mod_a] = [i]
    print("No")
