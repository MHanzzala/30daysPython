import csv


with open("data_0.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])



with open("data_0.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



with open("data_0.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])



with open("data_0.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open("data_0.csv", "a") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"id": 123, "title": "New title"})

    def get_length(file_path):
         with open("data_0.csv") as csvfile:
            reader = csv.reader(csvfile)
            reader_list = list(reader)
            print(reader_list)
            return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
            })



append_data("data.csv", "Justin", "hello@teamcfe.com")