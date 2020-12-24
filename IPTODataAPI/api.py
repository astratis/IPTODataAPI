import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class API:
    def __init__(self, file_type=None, start_date=None, end_date=None):
        self.base_url = 'https://www.admie.gr/getOperationMarketFile'
        self.resource_url = 'https://www.admie.gr/getFiletypeInfoEN'
        self.file_type = file_type
        self.start_date = start_date
        self.end_date = end_date
        self.check_file_type()

        if start_date != end_date:
            self.base_url += 'wRange'

    def get_file_types(self):
        r = requests.get(self.resource_url)
        file_types = []
        for i in r.json():
            file_types.append(i['filetype'])
        return file_types

    def check_file_type(self):
        self.file_types = self.get_file_types()
        if self.file_type in self.file_types:
            logger.info('Collecting data for {}...'.format(self.file_type))
        else:
            logger.warning('The file type is not correct, please use one of the following: {}'.format(self.file_types))

    @staticmethod
    def _create_postfix(params):
        return '&'.join(['%s=%s' % (k, v) for k, v in params.items()])

    def _url(self, params):
        postfix = self._create_postfix(params)
        return self.base_url + '?' + postfix

    def get_files(self):
        params = dict(dateStart=self.start_date, dateEnd=self.end_date, FileCategory=self.file_type)
        for key, value in dict(params).items():
            if value is None:
                del params[key]
        data_url = self._url(params)
        r = requests.get(data_url)
        files = []
        for i in r.json():
            files.append(i['file_path'])
        return files
