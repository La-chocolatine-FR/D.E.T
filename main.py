print("\n\
             \033[33m█▀▄   \033[35m██▀   \033[31m▀█▀\n\
             \033[33m█▄▀ \033[36m▄ \033[35m█▄▄ \033[37m▄  \033[31m█")
print("				  ")
print("        \033[33mDecide, \033[35mEvaluate, \033[31mTerminate")
print("				  ")
print("\033[32mhttps://github.com/La-chocolatine-FR/D.E.T\033[37m")
print("				  ")
print("[1]	")
print("[2]	Data reader")
print("[3]	")
print("[4]	")
print("[s/4]	exit")

terminal_launched = True
user_command = ""

while terminal_launched:
    user_command = input("=> ")

    if user_command == "aba":
        print("1")

    elif user_command == "2":
        exec(open("AAA/data-reader.py").read())

    elif user_command == "3":
        print("3")
    
    elif user_command == "help":
        print("\
-------------------------------------\n\
LISTE DES COMMANDES DISPONIBLES\n\
-------------------------------------\n\
s or 4 : Fermer le terminal\n\
-------------------------------------")

    elif user_command in {"s", "4"}:
        terminal_launched = False

    else:
        print("Commande introuvable...")
