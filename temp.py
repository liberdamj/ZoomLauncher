import csv

with open('class_file.csv', mode='w') as class_file:
    writer = csv.writer(class_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['98918113935', '127237'])
    writer.writerow(['93648280090', '6h955q'])
    writer.writerow(['97062598328', '956487'])