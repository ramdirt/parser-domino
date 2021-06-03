class Settings():
    def __init__(self):
        self.urls_lever_assembly = ['https://www.domino-group.com/tommaselli/en/lever-assembly-on-road.html',
                             'https://www.domino-group.com/tommaselli/en/lever-assembly-off-road.html',
                             'https://www.domino-group.com/tommaselli/en/lever-assembly-trial.html',
                             'https://www.domino-group.com/tommaselli/en/lever-assembly-scooter.html',
                             'https://www.domino-group.com/tommaselli/en/lever-assembly-vintage.html',
                             'https://www.domino-group.com/tommaselli/en/lever-assembly-speedway.html']
        self.url_catalog = 'https://www.domino-group.com/tommaselli/en/lever-assembly-on-road.html'
        self.url_domen = 'https://www.domino-group.com'
        self.money = 89
        self.file_save = 'csv/' + self.url_catalog.split('/')[-1][0:-5] + '.csv'
        self.file_error_save = 'file_error_save.csv'
        self.file_were_added = 'file_were_added.csv'
        self.file_translate_word = 'translate/translate.csv'
        self.range_max = None
        self.range_min = 0