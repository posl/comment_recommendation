def main():
    s = input()
    i = 0
    while i < len(s):
        if s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i+1 < len(s) and s[i+1] in "0123456789":
                if i+6 < len(s) and s[i+6] in "0123456789":
                    if i+7 < len(s) and s[i+7] in "0123456789":
                        if i+8 < len(s) and s[i+8] in "0123456789":
                            if i+9 < len(s) and
