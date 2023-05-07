def main():
    S = input()
    T = input()
    if S in T[:len(T)-1]:
        print("Yes")
    else:
        print("No")
