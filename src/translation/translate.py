import requests
import os

API_KEY = ''

class translation():
    def __init__(self, file):
        self.file = file

    def translate(self):
        with open('../../data/en/{}'.format(self.file), 'r') as f:
            self.source_file_l = f.read()
            #print(self.source_file)
        
        url = 'https://api-free.deepl.com/v2/translate'
        params = {
            'auth_key': API_KEY,
            'text': self.source_file_l,
            'source_lang': 'EN',
            'target_lang': 'FR'
        }

        request = requests.post(url, data=params)
        result = request.json()
        #print(result)
        
        with open('../../data/fr/{}'.format(self.file), 'w') as f:
            f.write(result['translations'][0]['text'])
        
        
        



if __name__ == '__main__':
    path = '../../data/en/'
    files = os.listdir(path)
    files = sorted(files)
    for i in range(1, 100):
        print(files[i])
        t = translation(files[i])
        t.translate()