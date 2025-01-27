from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Substitua pela sua chave API do Telegram
api_key = '7973285242:AAELW9YAijEPaZnozOiJ61eq_-WjQGxHXYY'

# Função que será chamada quando o comando /start for enviado ao bot
def start(update, context):
    update.message.reply_text("Olá! Eu sou o bot Coffeeswap!")

# Configuração do Updater para gerenciar as mensagens
updater = Updater(api_key, use_context=True)

# Adicionando o handler para o comando /start
updater.dispatcher.add_handler(CommandHandler('start', start))

# Inicia o bot
updater.start_polling()

# Deixa o bot funcionando indefinidamente
updater.idle()
