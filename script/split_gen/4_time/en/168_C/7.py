def main():
    A, B, H, M = map(int, input().split())
    # 12時間で360度、1時間で30度、1分で0.5度
    # 時針は分針を巻き込んでいるので、分針の分だけ時針の角度もずれる
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度
