from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot("TestBot")

trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train([
#     "hi",
#     "Welcome, friend 🤗"
# ])
# trainer.train([
#     "are you at test bot?",
#     "NO! Who told you that!!"
# ])
trainer.train(
    # 'chatterbot.corpus.english',
    'chatterbot.corpus.nature'
)

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
