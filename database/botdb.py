import sqlite3

conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE commands
             (user_id text, guild_id text, command text)''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()