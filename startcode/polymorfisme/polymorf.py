from voertuig import Voertuig
from fiets import Fiets
from auto import Auto

# 1. Maak een lijst van voertuigen
list = [Voertuig("onbekend voertuig", 562)
        ,Fiets("Gazelle", 23)
        ,Auto("Volkswagon", 78,100)]

# 2. Overloop de lijst en roep voor elk voertuig de methode beweeg() op
for voertuig in list:
        print(voertuig.beweeg())