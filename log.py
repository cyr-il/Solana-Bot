import discord_notify as dn 

def discord(message):
    notifier = dn.Notifier('https://discord.com/api/webhooks/974831319353794620/ZSx2g8Gtf0DphQn8eUAyNfTovrGESyOu1gOqhGJat1s8WR1VCHQmBaoRAGNUyRLddUCj')
    notifier.send(message, print_message=False)