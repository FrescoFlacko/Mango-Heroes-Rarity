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
            "Hat": {},
            "Weapon 1": {},
            "Weapon 2": {},
            "Weapon 3": {},
            "Affinity": {},
            "Special Edition": {}
        }

        for row in reader: 
            if row[1] == "Background":
                continue
            print("Generating " + row[0])
            for i, key in enumerate(rarities.keys()):
                rarities[key][row[i + 1]] = 1 if (row[i + 1] in rarities[key]) == False else rarities[key][row[i + 1]] + 1
        
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
            
            
        