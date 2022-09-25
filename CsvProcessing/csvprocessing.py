import csv


class CsvProcessing:

    def __init__(self):
        self.payload_files = []
        self.last_payload_files = []
        self.dict_files = {}
        self.after_processing_dict = {}
        self.last_payload = {}

    def read_csv(self):
        """
        this is in charge to read the csv from input folder
        :return: payload_files
        """
        with open('../input/players_sumary.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.dict_files = {'Song': row['Song'], 'Date': row['Date'],
                                   'Song-Date': row['Song'] + ',' + row['Date'],
                                   'Number of Plays': int(row['Number of Plays'])}

                self.payload_files.append(self.dict_files)

    def process_csv(self):
        """
        process_csv do the group by using searching into the payload
        :return: after_processing_dict
        """
        for i in self.payload_files:
            if self.after_processing_dict.get(i['Song-Date']) is not None:
                # If the value exist, sum to the key the value
                self.after_processing_dict[i['Song-Date']] += i['Number of Plays']
            else:
                # if the value does not exist, assign new key with a value
                self.after_processing_dict[i['Song-Date']] = i['Number of Plays']

    def send_processed(self):
        """
        Send the payload or dict processed
        :return: last_payload_files
        """
        for i in self.after_processing_dict.items():
            new = i[0].split(sep=',')

            self.last_payload = {'Song': new[0],
                                 'Date': new[1],
                                 'Total Number of Plays for Date': i[1]}

            self.last_payload_files.append(self.last_payload)
        return self.last_payload_files

    def transform_to_csv(self):
        """
        convert the dict to csv and write the file in ../output/people.csv
        :return: ../output/people.csv
        """
        keys = self.last_payload_files[0].keys()

        with open('../output/people.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.last_payload_files)


if __name__ == "__main__":
    c = CsvProcessing()
    c.read_csv()
    c.process_csv()
    c.send_processed()
    c.transform_to_csv()
