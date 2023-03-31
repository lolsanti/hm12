"""
class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def create_attribute(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            attribute = [line.rstrip('\n').lstrip('.') for line in lines]
            self.attribute = attribute


file_processor = FileProcessor('domains.txt')
file_processor.create_attribute()
print(file_processor.attribute)

"""

##############################################################

"""

class SurnameExtractor:
    def __init__(self, filename):
        self.filename = filename

    def get_surnames(self):
        with open(self.filename, 'r') as file:
            surnames = []
            for line in file:
                data = line.strip().split('\t')
                surname = data[1]
                surnames.append(surname)
        return surnames

extractor = SurnameExtractor('names.txt')
surnames = extractor.get_surnames()
print(surnames)

"""
##############################################################

"""

import re

class DateExtractor:
    def __init__(self, filename):
        self.filename = filename
        self.date_regex = re.compile(r'\b\d{1,2}(st|nd|rd|th)? [a-zA-Z]+ \d{4}\b')

    def extract_dates(self):
        dates = []
        with open(self.filename, 'r') as f:
            for line in f:
                match = self.date_regex.search(line)
                if match:
                    dates.append({"date": match.group()})
        return dates

date_extractor = DateExtractor('authors.txt')
dates = date_extractor.extract_dates()
print(dates)

"""

##############################################################
"""

from datetime import datetime


class MyClass:
    def get_date_list(self, file_name):
        date_list = []
        with open(file_name, 'r') as f:
            for line in f:
                date_original = line.strip()
                try:
                    date_obj = datetime.strptime(date_original, '%d %B %Y')
                    date_modified = date_obj.strftime('%d/%m/%Y')
                except ValueError:
                    date_modified = None

                date_dict = {"date_original": date_original, "date_modified": date_modified}
                date_list.append(date_dict)
        return date_list

my_object = MyClass()
file_name = "authors.txt"
date_list = my_object.get_date_list(file_name)

for date_dict in date_list:
    print(date_dict["date_original"], "->", date_dict["date_modified"])

"""






















