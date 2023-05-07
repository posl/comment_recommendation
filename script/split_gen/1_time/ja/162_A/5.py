def main():
    N = int(input())
    if N//100 == 7 or N%100//10 == 7 or N%10 == 7:
        print("Yes")
    else:
        print("No")
