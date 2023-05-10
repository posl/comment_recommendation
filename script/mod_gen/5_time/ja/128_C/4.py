def check_light(light, switch):
    #lightのスイッチの数だけforを回す
    for i in range(light[0]):
        #もしスイッチがonならcountを1増やす
        if s[light[i+1]-1] == 1:
            count += 1
    #countがlightの数の半分より大きいならばTrueを返す
    if count > light[0]//2:
        return True
    else:
        return False

if __name__ == '__main__':
    check_light()