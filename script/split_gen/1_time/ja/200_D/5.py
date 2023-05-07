def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    mod_dict = {}
    for i in range(N):
        mod_dict[i] = A[i] % mod
    for i in range(N):
        for j in range(i+1, N):
            if mod_dict[i] == mod_dict[j]:
                print("Yes")
                print("1 {}".format(i+1))
                print("1 {}".format(j+1))
                return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if mod_dict[i] == mod_dict[j] == mod_dict[k]:
                    print("Yes")
                    print("2 {} {}".format(i+1, j+1))
                    print("1 {}".format(k+1))
                    return
    print("No")
