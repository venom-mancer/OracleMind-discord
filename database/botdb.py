import sqlite3

conn = sqlite3.connect('sqlite3.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE commands
             (user_name char,user_id int, guild_id int, command text)''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()