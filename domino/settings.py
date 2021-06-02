class Settings():
    def __init__(self):
        self.url_catalog = 'https://www.domino-group.com/tommaselli/en/grips-atv.html'
        self.url_domen = 'https://www.domino-group.com'
        self.money = 89
        self.file_save = 'csv/' + self.url_catalog.split('/')[-1][0:-5] + '.csv'
        self.file_error_save = 'file_error_save.csv'
        self.file_were_added = 'file_were_added.csv'
        self.file_translate_word = 'translate/translate.csv'
        self.range_max = None
        self.range_min = 0