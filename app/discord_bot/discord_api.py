from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
required_command = '!gandalf'

gandalf_phrases = [
    "Tout ce que nous devons décider, c'est que faire du temps qui nous est imparti.",
    "Le voyage ne s'achève pas ici.",
    "La mort n'est qu'un autre chemin qu'il nous faut tous prendre.",
    "Le rideau de pluie grisâtre de ce monde s'ouvrira et tout sera brillant comme l'argent.",
    "L'espoir s'est embrasé.",
    "Je vous aspirerai Saroumane, comme on aspire le poison d'une plaie.",
    "Attendez ma venue aux premières lueurs du cinquième jour. À l'aube, regardez à l'Est.",
    "Vous ne passerez PAS!",
    "Il y a d'autres forces à l'oeuvre dans ce monde, à part la volonté du mal.",
    "Je crois que ce sont les petites choses, les gestes quotidiens des gens ordinaires qui nous préservent du mal.",
    "Un magicien n'est jamais en retard, Frodon Saquet, ni en avance d'ailleurs, il arrive précisément à l'heure prévue.",
    "C'est dans les hommes que nous devons placer notre espoir.",
    "Je suis serviteur du Feu Secret, détenteur de la flamme d'Anor. Le feu sombre ne vous servira à rien, flamme d'Udûn. Repartez dans l'ombre.",
    "Fuyez, pauvres fous!",
    "La bataille du gouffre de Helm est terminée. Celle pour la Terre du Milieu de fait que commencer.",
    "Crétin de touque!",
    "Nombreux sont les vivants qui mériteraient la mort. Et les morts qui mériteraient la vie. Pouvez-vous la leur rendre? Alors, ne soyez pas trop prompt à dispenser la mort en jugement. Mêmes les grands sages ne peuvent connaître toutes les fins.",
    "Et qui brise quelque chose pour découvrir ce que c'est, a quitté la voie de la sagesse.",
    "Je ne vous dirais pas de ne pas pleurer car toutes les larmes ne sont pas un mal.",
    "Rappelez vous Bilbon, le vrai courage n'est pas de savoir quand supprimer une vie, mais quand en épargner une.",   
]

def random_phrase(phrases):
    random_int = random.randint(0, len(phrases) - 1)
    return phrases[random_int]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Successfully logged in as: ', self.user)

    async def on_message(self, message):
        print(message.content)

        if message.author == self.user:
            return
        
        command, user_message = None, None

        if message.content.startswith(required_command):
            command = message.content.split(' ')[0]
            user_message = message.content.replace(required_command, '')
            print(command, user_message)

        if command == required_command:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f'**Hoki** {message.author.mention} **...** {bot_response} \n \n**«{random_phrase(gandalf_phrases)}»**')

intents  = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)