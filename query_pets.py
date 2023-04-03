import sqlite3

# Load the amended pets.db file ...
conn = sqlite3.connect('pets.db')
c = conn.cursor()

# Ask the user to enter a person's ID ...
person_id = int(input('Enter a person\'s ID number (enter -1 to quit): '))

# While loop until -1 is entered ...
while person_id != -1:
    c.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person_data = c.fetchone()
    
    # if person exists print their data.
    if person_data is not None:
        print('{} {} ({} years old)'.format(person_data[1], person_data[2], person_data[3]))
        
        c.execute('''
            SELECT pet.name, pet.age
            FROM person_pet
            JOIN pet ON person_pet.pet_id = pet.id
            WHERE person_pet.pet_id = ?
        ''', (person_id,))
        pets_data = c.fetchall()
        
        if pets_data:
            print('Owned pets:')
            for pet_data in pets_data:
                print('{} ({})'.format(pet_data[0], pet_data[1]))
        else:
            print('No data found for this person.')
    
    # If person does not exist, print an error message
    else:
        print('Error: Person with ID number {} does not exist.'.format(person_id))
    
    # Prompt user for person ID again
    person_id = int(input('Enter a person\'s ID number (enter -1 to quit): '))

# Close database connection
conn.close()
