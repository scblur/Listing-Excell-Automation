import pyexcel
a_list_of_dictionaries = [
     {
         "Name": 'Adam',
         "Age": 28
     },
     {
         "Name": 'Beatrice',
         "Age": 29
     },
     {
         "Name": 'Ceri',
         "Age": 30
     },
     {
         "Name": 'Dean',
         "Age": 26
     }
 ]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xlsx")

records = pyexcel.iget_records(file_name="your_file.xlsx")
print(type(records))

for record in records:
    print("%s is aged at %d" % (record['Name'], record['Age']))

# search_field = 'Name'
# search_sub_field = 'Beatrice'

for record in records:
    # print(type(record['Name']))
    # if record[search_field] == record[search_sub_field]:
    #     print("oh hi, it's me!! | ")
    print("%s is aged at %d" % (record['Name'], record['Age']))

pyexcel.free_resources()
