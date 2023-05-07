def main():
    N = int(input())
    w = []
    for i in range(N):
        w.append(input())
    #print(w)
    if len(w) != len(set(w)):
        print("No")
        return
    for i in range(N-1):
        if w[i][-1] != w[i+1][0]:
            print("No")
            return
    print("Yes")
