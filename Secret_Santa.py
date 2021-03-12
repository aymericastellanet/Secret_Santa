import random

participants = []

first_participant = input("Tapez le nom d'un participant :\n").capitalize()

participants.append(first_participant.strip())

new_participant = ""

while new_participant != "Exit":
    if new_participant.strip() != "":
        participants.append(new_participant.strip())
    new_participant = input("Tapez le nom d'un autre participant ou 'exit' pour sortir : \n").capitalize()

print("------------------")

message = ""
part_give = participants[:] #list of participants giving a gift
part_receive = participants[:] #list of participants receiving a gift

while part_give != [] and part_receive != []:
    g = random.randint(0, len(part_give)-1)
    r = random.randint(0, len(part_receive)-1)
    
    if part_give[g] != part_receive[r]:
        giver = part_give.pop(g)
        receiver = part_receive.pop(r)
        message += "{} offre un cadeau à {} !\n".format(giver, receiver)
    
    elif (part_give[g] == part_receive[r]) and (len(part_give) == 1 and len(part_receive) == 1):
        # S'il ne reste plus qu'une seule et même personne dans la liste 'part_give' et 'part_receive'
        # alors on réinitialise les variables et on recommence.
        # ça permet d'éviter le bug d'être bloqué dans la boucle while et alors qu'il ne reste qu'une personne.
        message = ""
        part_give = participants[:]
        part_receive = participants[:]


print(message)
print("MERRY CHRISTMAS!!! OH, OH, OH!")
