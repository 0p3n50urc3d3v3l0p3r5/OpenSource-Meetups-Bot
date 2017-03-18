# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import configparser
import logging
from telegram import ChatAction

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('bot.ini')


updater = Updater(token=config['BOT']['TOKEN'])
dispatcher = updater.dispatcher
help_text="""
[ x ] /invitelink  --> Prints the invite link to this group
[ x ] /googleform  --> Link to the Google Form
[ x ] /googlegroup  --> Link to the Google Group
[ x ] /facebook    --> Facebook Group of Open3Source
"""

def invitelink(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['invite_link'])

def fbgroup(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['fbgroup'])

def googleform(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['googleform'])

def googlegroup(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['googlegroup'])

def teams(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''
/SocialMediaTeam 
/WebsiteDesignteam 
/WebDevelopment 
/GraphicDesignTeam 
/BotTeam 
/TeamManage  
''')

def SocialMediaTeam(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''SocialMediaTeam
 uditwapt
 Please use '@' at the start of each username to ping them. ''')

def WebsiteDesignteam(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''
 We are looking for passionate, talented people to join our team
''')

def WebDevelopment(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''
  We are looking for passionate, talented people to join our team
''')

def GraphicDesignTeam(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''
 We are looking for passionate, talented people to join our team 
''')

def BotTeam(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''BotTeam
 namanmadan  theparadoxer02
 Please use '@' at the start of each username to ping them.
''')

def TeamManage(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='''TeamManage
 uditwapt  sndy96
 Please use '@' at the start of each username to ping them.
''')

def help(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=help_text,parse_mode='Markdown')

invite_handler = CommandHandler('invitelink',invitelink)
teams_handler = CommandHandler('teams',teams)
fbgroup_handler = CommandHandler('facebook',fbgroup)
googleform_handler = CommandHandler('googleform',googleform)
GraphicDesignTeam_handler = CommandHandler('GraphicDesignTeam',GraphicDesignTeam)
googlegroup_handler = CommandHandler('googlegroup',googlegroup)
WebDevelopment_handler = CommandHandler('WebDevelopment',WebDevelopment)
SocialMediaTeam_handler = CommandHandler('SocialMediaTeam',SocialMediaTeam)
WebsiteDesignteam_handler = CommandHandler('WebsiteDesignteam',WebsiteDesignteam)
BotTeam_handler = CommandHandler('BotTeam',BotTeam)
TeamManage_handler = CommandHandler('TeamManage',TeamManage)
help_handler = CommandHandler('help',help)

dispatcher.add_handler(invite_handler)
dispatcher.add_handler(teams_handler)
dispatcher.add_handler(fbgroup_handler)
dispatcher.add_handler(googleform_handler)
dispatcher.add_handler(GraphicDesignTeam_handler)
dispatcher.add_handler(WebDevelopment_handler)
dispatcher.add_handler(SocialMediaTeam_handler)
dispatcher.add_handler(WebsiteDesignteam_handler)
dispatcher.add_handler(BotTeam_handler)
dispatcher.add_handler(TeamManage_handler)
dispatcher.add_handler(googlegroup_handler)
dispatcher.add_handler(help_handler)


updater.start_polling()
updater.idle()
