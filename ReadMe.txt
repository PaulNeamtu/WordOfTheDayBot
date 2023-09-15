The code for this bot requires 2 components before it can work properly.

1) an active bot
-a discord bot must be created and its token must be copy pasted into the on_message function in the bot.py code

2) a discord server
-there must be a place for the bot to send messages
-the channel ID must be copy pasted into the on_message function in the bot.py code as well


Functionality of the bot
-The bot will post a word of the day message in the specified channel every day at 14:30 UTC (This can be changed in the bot.py code)
-The word and definition are taken from the Marriam-Webster Word of the Day website.
-If another member of the server post the message "!context" in the same specified channel, the bot will post the word in context. This context is also taken from the Marriam-Webster website.
-If another member of the server post the message "!funfact" in the same specified channel, the bot will post a fun fact about the word of the day. This fact is also taken from the Marriam-Webster website.

