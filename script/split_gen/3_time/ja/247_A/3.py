def main():
    S = input()
    S_list = list(S)
    S_list.append("0")
    S_list.pop(0)
    print("".join(S_list))
