def main():
    N = int(input())
    #print("N = ", N)
    for i in range(1, 10):
        for j in range(1, 10):
            #print("i = ", i, "j = ", j, "i*j = ", i*j)
            if i*j == N:
                print("Yes")
                return
    print("No")
    return
