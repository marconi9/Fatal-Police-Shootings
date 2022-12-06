data_file = open("fatal-police-shootings-data.csv", 'r')

#separating the rows (victims) of the data into lines
data_lines = data_file.readlines()

#creating empty dictionary
database = {} 
for row in range(1, len(data_lines)): 
    line = data_lines[row]
#splits the line into columns (variables)
    entries = line.split(',') 
    db_entry = {}
#connecting each value to the key(variable)
    db_entry["name"] = entries[1] 
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0])
#connecting each set of keys/values (db_entry) to the victim's ID
    database[entry_id] = db_entry 

#print ID 1694
print ((database[1694])["name"])

#print the name of all subjects of fatal police shootings in Minnesota 
minnesota_killings = []
for person in database:
    if (database[person])["state"] == "MN": 
        minnesota_killings.append((database[person])["name"])
print(minnesota_killings)

#Create a new dictionary, called race counts
race_counts = {}
for people in database:
    race = (database[people])["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

#Print the fraction of fatal police shootings with a black subject
print(race_counts["B"] / len(database))

#create dictionary of unarmed victims
unarmed_victims = {}
for person in database:
    if (database[person])["armed"] == "unarmed":
        unarmed_victims[person] = database[person]

#create dictionary of unarmed victims by race
unarmed_race_counts = {}
for person in unarmed_victims:
    race = (unarmed_victims[person])["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

#print proportion for black unarmed victims to total unarmed victims
print(unarmed_race_counts["B"] / len(unarmed_victims))
