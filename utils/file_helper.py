class File():
    def write_to_file(self, path, text):
        f = open(path, 'a', encoding='UTF-8')  # './1.txt'
        # text = f.read()
        # text = [i for i in text.split(',')]
        #f.writelines(text)
        f.write(f'{text}\r')
        f.close()
