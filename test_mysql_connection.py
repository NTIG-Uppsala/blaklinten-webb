"""
Beskrivning av denna modul: 
- Vad modulen gör
- Hur den används
- Eventuella andra viktiga detaljer
"""

import mysql.connector

try:
    # Anslut till MySQL-databasen på din webbserver
    connection = mysql.connector.connect(
        host="blaklinten-db.mysql.database.azure.com",
        user="Overlord",
        password="Blaklinten123",
        database="blaklinten-info",
    )

    if connection.is_connected():
        print("Anslutning till databasen lyckades!")
        connection.close()
    else:
        print("Kunde inte ansluta till databasen.")

except mysql.connector.Error as error:
    print(f"Kunde inte ansluta till databasen: {error}")
