import mysql.connector
from mysql.connector import Error

hostInput = input('What host to connect to (localhost): ')
portInput = input('What port to connect to (3306): ')
usernameInput = input('What uesr to connect with (root): ')
passwordInput  = input('What password to connect with: ')




def primary_word():
    mycursor.execute("SELECT * FROM word WHERE word LIKE (%s)", (wordInput, ))
    wordFound = mycursor.fetchall()
    return wordFound

def word_not_found(inputWord):
    print(f'The word {inputWord} was not found... adding')
    mycursor.execute("INSERT INTO dictionary.word VALUES (%s)", (inputWord,))
    mydb.commit()
    print(f'Added {inputWord} to the database')
    quit()

def word_found(inputWord):
    print(f'Found {inputWord} in the database.')
    print(f"('{inputWord}')")
    newWord = input(f'Change {inputWord} To: ')
    mycursor.execute("UPDATE word SET word = (%s) WHERE word = (%s)", (newWord, inputWord))
    mydb.commit()
    print(f'Changed "{inputWord}" to: {newWord}')
    quit()

try:

    mydb = mysql.connector.connect(
        host=hostInput,
        port=portInput,
        user=usernameInput,
        passwd=passwordInput,
        auth_plugin="mysql_native_password",
        database='dictionary')

    mycursor = mydb.cursor()

    mycursor.execute("SHOW VARIABLES like 'version'")
    myVersion = mycursor.fetchall()
    for version in myVersion:
        print(f'Connected succesfully')
        print(version)
    


    



    wordInput = input("What word do you want to add/change: ")
    word = primary_word()
    
    
    if len(word) == 0:
        word_not_found(wordInput)

    else:
        word_found(wordInput)


except Error as e:
    print(f"Could not login with user/password provided. {e}")
    exit()
