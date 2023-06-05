def main():
    s = input()
    if s[0] >= 'A' and s[0] <= 'Z' and s[-1] >= 'A' and s[-1] <= 'Z':
        if len(s) == 8:
            if s[1] >= '0' and s[1] <= '9':
                if s[2] >= '0' and s[2] <= '9':
                    if s[3] >= '0' and s[3] <= '9':
