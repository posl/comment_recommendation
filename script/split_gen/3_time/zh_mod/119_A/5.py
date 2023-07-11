def main():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[1]) < 4:
