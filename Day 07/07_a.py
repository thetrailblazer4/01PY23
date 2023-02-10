import csv


# with open('new_demo.csv') as csv_file:
# 	csv_r = csv.DictReader(csv_file)

# 	for line in csv_r:
# 		print(line['email'])


with open('new_demo.csv', 'r') as csv_file:
	csv_r = csv.DictReader(csv_file)

	with open('new_demo_copy.csv', 'w') as new_file:

		fieldnames = ['first_name','last_name']
		csv_w = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter='\t')

		for line in csv_r:
			del line['email']
			csv_w.writerow(line)
