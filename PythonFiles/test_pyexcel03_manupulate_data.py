import pyexcel as p
def increase_everyones_age(generator):
    for row in generator:
        row['Age'] += 1
        yield row
def duplicate_each_record(generator):
    for row in generator:
        yield row
        yield row
records = p.iget_records(file_name="your_file.xlsx")
io=p.isave_as(records=duplicate_each_record(increase_everyones_age(records)),
dest_file_type='csv', dest_lineterminator='\n')
print(io.getvalue())
