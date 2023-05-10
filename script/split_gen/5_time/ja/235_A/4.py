def main():
    # 標準入力の受け取り
    abc = input()
    # 処理
    bca = abc[1] + abc[2] + abc[0]
    cab = abc[2] + abc[0] + abc[1]
    result = int(abc) + int(bca) + int(cab)
    # 結果
    print(result)
