"""
Takes a csv file as input having certain format
Convert each row of the file into vcard format and write them in a file.

CSV Format:
Name, PhoneNumber, Email

First line of csv is skipped for header if skipFirst = True
"""

import csv


skipFirst = True


def csv_to_vcf(csv_file, vcf_file):
    with open(csv_file, "r", newline="", encoding="utf-8") as csvfile, open(
        vcf_file, "w", encoding="utf-8"
    ) as vcf:
        csvreader = csv.reader(csvfile)
        if skipFirst:
            next(csvreader)  # Skip header if exists

        for row in csvreader:
            name, phone_number, email = row
            vcf.write("BEGIN:VCARD\n")
            vcf.write("VERSION:3.0\n")
            vcf.write(f"FN:{name}\n")
            vcf.write(f"TEL;TYPE=CELL:{phone_number}\n")
            vcf.write(f"EMAIL;TYPE=INTERNET:{email}\n")
            vcf.write("END:VCARD\n")


if __name__ == "__main__":
    csv_file = "output.csv"  # Provide the name of your CSV file
    vcf_file = "contacts.vcf"  # Name for the output VCF file
    csv_to_vcf(csv_file, vcf_file)
    print(f"Conversion complete. VCF file saved as '{vcf_file}'")
