import mysql.connector
from tabulate import tabulate

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",  # ou l'adresse IP de ton serveur MySQL
    user="root",       # nom d'utilisateur
    password="",       # mot de passe vide
    database="det"     # nom de la base de données
)

# Créer un curseur pour interroger la base de données
cursor = conn.cursor()

# Demander à l'utilisateur de saisir un groupe sanguin
group = input("Entrez un groupe sanguin (ex: AB+, O-, etc.): ")

# Récupérer la liste des tables dans la base de données
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Variable pour savoir si le groupe sanguin a été trouvé
found = False

# Liste pour stocker les résultats
results = []

# Parcourir toutes les tables
for table in tables:
    table_name = table[0]
    
    # Vérifier si la table contient une colonne 'blood_type'
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = cursor.fetchall()
    columns_names = [col[0] for col in columns]
    
    if 'blood_type' in columns_names:
        # Construire et exécuter la requête de recherche dans cette table
        try:
            cursor.execute(f"SELECT * FROM {table_name} WHERE blood_type = %s", (group,))
            rows = cursor.fetchall()
            
            # Si le groupe sanguin est trouvé dans cette table
            if rows:
                found = True
                # Ajouter les résultats de la table à la liste
                for row in rows:
                    results.append([table_name] + list(row))  # Ajouter le nom de la table et les résultats de la ligne
        except mysql.connector.Error as err:
            # Si une erreur se produit, ignorer et passer à la table suivante
            print(f"Erreur lors de l'exécution de la requête sur la table {table_name}: {err}")

# Afficher les résultats sous forme de tableau si le groupe sanguin est trouvé
if found:
    print(f"\nRésultats pour le groupe sanguin {group} :\n")
    # Afficher un joli tableau avec tabulate
    headers = ['Table', 'Blood Type', 'Rarity Level', 'Quantity']  # En-têtes de colonnes
    print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
else:
    print(f"Aucune donnée trouvée pour le groupe {group} dans aucune des tables.")

# Fermer la connexion
cursor.close()
conn.close()
