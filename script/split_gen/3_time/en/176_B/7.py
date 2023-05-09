def main():
    N = input()
    if N == '0':
        print("Yes")
        return
    if int(N[-1]) % 2 == 0:
        print("No")
        return
    if sum([int(i) for i in N]) % 9 == 0:
        print("Yes")
    else:
        print("No")
