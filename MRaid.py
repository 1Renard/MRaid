import time
import discord
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = "Mr/")
status = cycle(["programme : Mraid", "Github : Malicioums"])

titre = ("\f────────────────────────────────────\n\
	....	     ....  ........\n\
	.....       .....  ..........\n\
	.......   .......  ...   ....\n\
	.... ....... ....  ..........\n\
	....  .....  ....  ....  ....\n\
	....   ...   ....  ....   ....\n\
	....    .    ....  ....    ....AID™\n\
\f────────────────────────────────────\n\
quit  : Quitter MRaid\n\
hraid : Afficher les commandes de raid\n\
info  : Donne les liens de MRaid \n\
menu  : Aller au menu principal (ici)\n\
		\f	MRaid by Malicioums\n\
\f────────────────────────────────────\f")

text_info = "\f────────────────────────────────────\n\
\f	....	     ....  ........\n\
	.....       .....  ..........\n\
	.......   .......  ...   ....\n\
	.... ....... ....  ..........\n\
	....  .....  ....  ....  ....\n\
	....   ...   ....  ....   ....\n\
	....    .    ....  ....    ....AID™\n\
\f	   créé part Malicioums\n\
\f────────────────────────────────────\n\
\fLien du serveur Discord :\n\
\fLien de la chaîne Youtube :\n\
\f────────────────────────────────────\f"

info_hraid = "\f┌───────────────────────┐\n\
│		    	     │\n\
│      Commandes de raid     │\n\
│                            │\n├───────────────────────┤\n\
│		             │\n\
│		             │\n\
├	run :                ┤\n\
│Sert à entrer le token      │\n\
│du bot.                     │\n\
│		             │\n\
├		             ┤\n\
│		             │\n\
│		             │\n\
├		             ┤\n\
│		             │\n\
│		             │\n\
└───────────────────────┘\f"


print(titre)
launched = True
nombre = 5
cmd = input("[-MRaid-] >> ")
token_test = ""
while launched:
	if cmd == "quit":
		print(f"[-MRaid-] Fermeture dans {nombre} seconde")
		time.sleep(1)
		nombre -= 1
	if nombre == 0:
		print("[-MRaid-] Vous avez quitté MRaid...")
		launched = False
	elif cmd == "info":
		print(text_info)
		cmd = input("[-MRaid-] >> ")
	elif cmd == "hraid":
		print(info_hraid)
		cmd = input("[-MRaid-] >> ")
	elif cmd == "menu":
		print(titre)
		cmd = input("[-MRaid-] >> ")
	elif cmd == "run":
		@client.event
		async def on_ready():
			change_status.start()
			print("\f┌──────────────────────────┐\n│	Bot connecter	         │\n│Nom du bot:", client.user.name,"         │" , "\n│ID du bot:", client.user.id, "  │", "\n└──────────────────────────┘\f")
		@tasks.loop(seconds=20)
		async def change_status():
			await client.change_presence(activity=discord.Game(next(status)))
		token_test = input("[-MRaid-] Entrer votre token : ")
		client.run(token_test)
	elif cmd == "spammeur":
		nombre_m = input("[-MRaid-] Entrer le nombre de message à spammer :")
		message_a = input("[-MRaid-] Entrer le message à spammer :")
		cmd = input("[-MRaid-] >> ")
		pass
	else:
		continue
#────────────────
#└────────────┘
#┌────────────┐
#│┤├https://discordapp.com/oauth2/authorize?client_id=653017570915516427&scope=bot&permissions=8