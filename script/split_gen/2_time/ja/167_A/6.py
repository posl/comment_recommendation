def main():
    S = input() #ID
    T = input() #新しいID
    if S == T[0:len(S)] and len(T) == len(S) + 1:
        print("Yes")
    else:
        print("No")
