import sqlite3

# Load the pets.db file 
conn = sqlite3.connect('pets.db')

# Specify the data for each table 
# person data 
person_data = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

# pet data 
pet_data = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

# person_pet data 
person_pet_data = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

# Load the data into each table 
conn.executemany('INSERT OR IGNORE INTO person VALUES (?, ?, ?, ?)', person_data)
conn.executemany('INSERT OR IGNORE INTO pet VALUES (?, ?, ?, ?, ?)', pet_data)
conn.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pet_data)



# Commit changes and close connection
conn.commit()
conn.close()