def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    modA = [a % 200 for a in A]
    modA_dict = {}
    for i, a in enumerate(modA):
        if a in modA_dict:
            modA_dict[a].append(i+1)
        else:
            modA_dict[a] = [i+1]
    for key in modA_dict:
        if len(modA_dict[key]) > 1:
            print("Yes")
            print(len(modA_dict[key]))
            print(" ".join([str(x) for x in modA_dict[key]]))
            print(len(modA_dict[key]))
            print(" ".join([str(x) for x in modA_dict[key]]))
            return
    print("No")
