import csv


class CsvProcessing:

    def __init__(self):
        self.payload_files = []
        self.last_payload_files = []
        self.dict_files = {}
        self.after_processing_dict = {}
        self.last_payload = {}

    def read_csv(self) -> list:
        with open('../media/players_sumary.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.dict_files = {'Song': row['Song'], 'Date': row['Date'],
                                   'Song-Date': row['Song'] + ',' + row['Date'],
                                   'Number of Plays': int(row['Number of Plays'])}

                self.payload_files.append(self.dict_files)

    def process_csv(self):

        for i in self.payload_files:
            if self.after_processing_dict.get(i['Song-Date']) is not None:
                # If the value exist, sum to the key the value
                self.after_processing_dict[i['Song-Date']] += i['Number of Plays']
            else:
                # if the value does not exist, assign new key with a value
                self.after_processing_dict[i['Song-Date']] = i['Number of Plays']

    def send_processed(self):
        for i in self.after_processing_dict.items():
            new = i[0].split(sep=',')

            self.last_payload = {'Song': new[0],
                                 'Date': new[1],
                                 'Total Number of Plays for Date': i[1]}

            self.last_payload_files.append(self.last_payload)
        print(self.last_payload_files)


if __name__ == "__main__":
    c = CsvProcessing()
    c.read_csv()
    c.process_csv()
    c.send_processed()
