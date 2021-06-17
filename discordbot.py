from discord.ext import commands
import os
import traceback
from datetime import datetime, timedelta

token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_voice_state_update(member, before, after):

    if member.guild.id == 852145141909159947 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(852153560993234974)
        if before.channel is None: 
            embed = discord.Embed(title="通話開始",color=0x42b3f5)
            embed.add_field(name="`チャンネル`",value = f'<#{after.channel.id}>')
            embed.add_field(name="`始めた人`",value = f'{member.mention}')
            embed.add_field(name="`開始時間`",value = f'{now:%Y/%m/%d \n %H:%M}')
            await alert_channel.send(embed=embed)
        elif after.channel is None: 
            embed = discord.Embed(title="通話開始",color=0xf54842)
            embed.add_field(name="`チャンネル`",value = f'<#{before.channel.id}>')
            embed.add_field(name="`始めた人`",value = f'{member.mention}')
            embed.add_field(name="`終了時間`",value = f'{now:%Y/%m/%d \n %H:%M}')
            await alert_channel.send(embed=embed)

bot.run(token)
