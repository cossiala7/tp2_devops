weeks = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
Days = input("Veuillez entrer le jour de la semaine: ")
if Days in ["lundi","mardi","mercredi"]:
 print("C'est le debut de semaine ")
elif Days in["jeudi" , "vendredi"]:
 print("souriez c'est bientot le week-end")
elif Days in["samedi","dimanche"]:
 print("c'est le week-end") 
else:
 print("ceci n'est pas un jour de la semaine")
 print("merci beaucoup")