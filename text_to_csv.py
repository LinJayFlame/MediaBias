import csv

input_file = f"data.txt"
output_file = f"data.csv"

# Open the txt file
file = open(input_file, 'r', encoding = "utf-8")
new_text = file.readlines()

text = [s for s in new_text if s != "\n"]
text2 = [s[:-1] for s in text]

# Open the csv file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write each sentence as a new row in the CSV
    for line in text2:
        writer.writerow([line])  # Write as a single column in CSV