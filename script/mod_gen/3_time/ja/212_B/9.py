def main():
    # 標準入力から暗証番号を取得
    passcode = input()
    # 暗証番号の4桁がすべて同じ数字の場合、弱い暗証番号とする
    if passcode[0] == passcode[1] and passcode[1] == passcode[2] and passcode[2] == passcode[3]:
        print("Weak")
        return
    # 暗証番号の4桁が連続している場合、弱い暗証番号とする
    if passcode[1] == str(int(passcode[0]) + 1) and passcode[2] == str(int(passcode[1]) + 1) and passcode[3] == str(int(passcode[2]) + 1):
        print("Weak")
        return
    # 暗証番号の4桁が連続している場合、弱い暗証番号とする
    if passcode[0] == "9" and passcode[1] == "0" and passcode[2] == "1" and passcode[3] == "2":
        print("Weak")
        return
    # どちらにも該当しない場合、強い暗証番号とする
    print("Strong")
    return

if __name__ == '__main__':
    main()