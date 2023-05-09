def main():
    N = int(input())
    #print(N)
    #print(sum(map(int, str(N))))
    if N % sum(map(int, str(N))) == 0:
        print("Yes")
    else:
        print("No")
