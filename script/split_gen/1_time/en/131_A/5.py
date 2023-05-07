def main():
    sec_code = input()
    if sec_code[0] == sec_code[1] or sec_code[1] == sec_code[2] or sec_code[2] == sec_code[3]:
        print("Bad")
    else:
        print("Good")
