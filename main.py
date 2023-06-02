from chatterbot import ChatBot
from chatterbot.trainers import ChatBotCorpusTrainer

chatbot = ChatBot('Harry Potter')

trainer = ChatBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Harry Potter: ', response)