"""
Converts RSP Processed CSV(by daddy) to new csv with Name, Number, Email as columns.
This output csv can be further used to produce vcf files.

RSP Processed CSV Format:
Name,Country,Province,District,Palika,Type,W,Tole,,F,,FP,Gender,EB,Party,Type,Post,DOB(BS),Code,Mobil,Email
Daya Ram Rana,Nepal,Supa,Kanchanpur,Punarbas,Napa,1,VT,F,1,FP,1,Male,Adj,RSP,VEM,Post,2049-08-12,977,9810662079,dayaramranarsp1@gmail.com

Name is formed by combining many of the columns with a '-' in between. Number and Email are kept are they are.
"""

import csv
import sys


CONTACT = 7
def process_csv(input_csv_file, output_csv_file):
    with open(input_csv_file, "r", newline="", encoding="utf-8") as csvfile, open(
        output_csv_file, "w", newline="", encoding="utf-8"
    ) as output:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(output)

        # Write header
        header = next(csvreader)
        csvwriter.writerow(["Name", "Number", "Email"])

        for row in csvreader:
            name = row[1]+ "-"+row[14]+"-"+row[15]+"-"+ "W"+ row[16]+"-RSP"
            

            number = row[CONTACT]  # Assuming phone number is in column 17 (adjust if needed)
            # email = row[20]  # Assuming email is in column 18 (adjust if needed)
            email = ''

            csvwriter.writerow([name, number, email])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.csv")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_csv_file = "output.csv"  # Output CSV file name
    process_csv(input_csv_file, output_csv_file)
    print(f"Processing complete. Result saved in '{output_csv_file}'")
