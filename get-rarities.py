#!usr/bin/python
import csv
import json

if __name__ == "__main__":
    with open('traits.csv', 'r', newline='') as csvReader:
        reader = csv.reader(csvReader)
        rarities = {
            "Background": {},
            "Stance": {},
            "Mango Colour": {},
            "Eyes": {},
            "Mouth": {},
            "Clothes": {},
            "Colour": {},
            "Hat": {}
        }

        for row in reader: 
            if row[1] == "Background":
                continue
            print("Generating " + row[0])
            rarities["Background"][row[1]] = 1 if (row[1] in rarities["Background"]) == False else rarities["Background"][row[1]] + 1
            rarities["Stance"][row[2]] = 1 if (row[2] in rarities["Stance"]) == False else rarities["Stance"][row[2]] + 1
            rarities["Mango Colour"][row[3]] = 1 if (row[3] in rarities["Mango Colour"]) == False else rarities["Mango Colour"][row[3]] + 1
            rarities["Eyes"][row[4]] = 1 if (row[4] in rarities["Eyes"]) == False else rarities["Eyes"][row[4]] + 1
            rarities["Mouth"][row[5]] = 1 if (row[5] in rarities["Mouth"]) == False else rarities["Mouth"][row[5]] + 1
            rarities["Clothes"][row[6]] = 1 if (row[6] in rarities["Clothes"]) == False else rarities["Clothes"][row[6]] + 1
            rarities["Colour"][row[7]] = 1 if (row[7] in rarities["Colour"]) == False else rarities["Colour"][row[7]] + 1
            rarities["Hat"][row[8]] = 1 if (row[8] in rarities["Hat"]) == False else rarities["Hat"][row[8]] + 1
        
        with open('rarities.json', 'w', encoding='utf-8') as f:
            json.dump(rarities, f, ensure_ascii=False, indent=4)

        with open('rarities.csv', 'w', newline='') as csvWriter:
            writer = csv.writer(csvWriter)
            row = []
            for attribute in rarities.keys():
                writer.writerow([attribute, 'Amount'])
                for value in rarities[attribute].keys():
                    rarities[attribute][value] = rarities[attribute][value] / 7000
                    writer.writerow([value, rarities[attribute][value]])
                writer.writerow([])
            
            
        