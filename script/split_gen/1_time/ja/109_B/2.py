def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(w) != len(set(w)):
        print("No")
        return
    for i in range(1, len(w)):
        if w[i-1][-1] != w[i][0]:
            print("No")
            return
    print("Yes")
    return
