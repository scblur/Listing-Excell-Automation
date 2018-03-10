import pyexcel as p
def increase_everyones_age(generator):
    for row in generator:
        row['Age'] += 1
        yield row

records = p.iget_records(file_name="your_file.xlsx")

io=p.isave_as(records=increase_everyones_age(records), dest_file_name="your_file2.xlsx" )

# p.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xlsx")

# print(io.getvalue())
