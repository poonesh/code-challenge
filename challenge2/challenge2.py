import csv
import datetime
current_year = datetime.datetime.now().year


def sorting_func(row):
    """
    This function returns a tuple to sort the rows. First by DeviceID
    and then by year, month and day.

    """
    device_id = 0
    year = 0
    month = 0
    day = 0
    infinity = float("inf")

    device_id = infinity if row[0] == "" else int(row[0])
    if row[5] == "":
        year = infinity
        month = infinity
        day = infinity
    else:
        date_arr = str(row[5]).split("/")
        if len(date_arr) == 3:
            year = int(date_arr[2])
            year += 2000 if year <= current_year else 1900
            month = int(date_arr[0])
            day = int(date_arr[1])
        else:
            date_arr = str(row[5]).split("-")
            year = int(date_arr[0])
            month = int(date_arr[1])
            day = int(date_arr[2])

    return (device_id, year, month, day)


def sort_csv(filename, output_filename):
    """
    This function read the csv file and sorts according to DeviceID and Date
    and writes out the final sorted file.
    """
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        with open(output_filename, 'w') as new_file:
            csv_writer = csv.writer(new_file)

            sortedData = sorted(csv_reader, key=sorting_func)
            csv_writer.writerow(header)
            for line in sortedData:
                csv_writer.writerow(line)

if __name__ == '__main__':
    sort_csv('large_data.csv', 'large_data_sorted.csv')
