def main():
    S = input()
    if S.islower() == False and S.isupper() == False and S.isalnum() == True:
        if len(S) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
