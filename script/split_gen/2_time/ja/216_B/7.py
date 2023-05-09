def main():
    N = int(input())
    names = list()
    for i in range(N):
        names.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i] == names[j]:
                print("Yes")
                return
    print("No")
    return
