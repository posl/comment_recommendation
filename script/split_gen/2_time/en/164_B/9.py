def main():
    #get input
    A, B, C, D = map(int, input().split())
    #calculate
    if B >= C*D:
        print("No")
    else:
        print("Yes")
