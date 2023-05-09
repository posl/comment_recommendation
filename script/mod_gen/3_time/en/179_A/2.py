def pluralize(noun):
    if noun.endswith('s'):
        return noun + 'es'
    else:
        return noun + 's'
print(pluralize('apple'))
print(pluralize('bus'))
print(pluralize('box'))

if __name__ == '__main__':
    pluralize()