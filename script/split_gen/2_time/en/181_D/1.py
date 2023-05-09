def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
        return
    if len(S) == 1:
        print('No')
        return
    if '3' in S:
        if '4' in S:
            print('Yes')
            return
        if '6' in S:
            print('Yes')
            return
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '5' in S:
            if '7' in S:
                print('Yes')
                return
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '4' in S:
        if '6' in S:
            print('Yes')
            return
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '5' in S:
            if '7' in S:
                print('Yes')
                return
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '5' in S:
        if '7' in S:
            print('Yes')
            return
        if '9' in S:
            print('Yes')
            return
        print('No')
        return
    if '6' in S:
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '7' in S:
        if '9'
