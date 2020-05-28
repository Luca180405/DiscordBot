import discord
from discord.ext import commands
import random
import asyncio
from discord.ext import tasks
import pytz
from datetime import datetime

client = commands.Bot(command_prefix='+')

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('auf Universe'))
    await asyncio.sleep(11)
    await client.change_presence(status=discord.Status.online, activity=discord.Game('https://discord.gg/VaBUjCe'))
    await asyncio.sleep(11)
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Ticket» ,createticket '))
    await asyncio.sleep(11)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f"Wilkommen auf diesem Server {member.mention}")
    role = discord.utils.get(member.guild.roles, name="Mitglied")
    await member.add_roles(role)

@client.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.channels, name="leave")
    await channel.send(f"{member.mention} musste uns leider verlassen :c")

coinantworten = ["Kopf", "Zahl"]

@client.command(aliases= ['Coinflip', 'Münzenwerfen', 'Münzwerfen'])
async def coinflip(ctx):
        mess = await ctx.send("Ich werfe die Münze")
        await asyncio.sleep(0.8)
        await mess.edit(content="Ich werfe die Münze.")
        await asyncio.sleep(0.8)
        await mess.edit(content="Ich werfe die Münze..")
        await asyncio.sleep(0.8)
        await mess.edit(content="Ich werfe die Münze...")
        await asyncio.sleep(0.8)
        await mess.edit(content="Es ist **{}**!".format(random.choice(coinantworten)))

@client.command(pass_context=True, aliases= ['befehle'])
async def help(ctx):
    embed = discord.Embed(title='<a:rechts2:714818731615846461>Hilfemenü zu Astro<a:links:714818796573163581>\nPrefix: `,`',
                          description='Reagiere mit 💿\nUm das Moderationsmenü zu öffen\n\nReagiere mit 🛠️\num das Funktionsmenü zu öffnen\n\nReagiere mit Reagiere mit <a:HappySquirtle:714387020775948349>\nUm das Fun Menü zu öffnen\n\nReagiere mit <:Wumpus:714900973956628481>\nUm das User Menü zu öffnen.', colour=0x0101df)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Angefordert von {ctx.author}", icon_url=ctx.author.avatar_url)

    mess = await ctx.author.send(embed= embed)

    await mess.add_reaction('💿')
    await mess.add_reaction('🛠️')
    await mess.add_reaction('<a:HappySquirtle:714387020775948349>')
    await mess.add_reaction('<:Wumpus:714900973956628481>')
    await ctx.send("Die Nachricht wurde dir per **DM** zugeschickt!")
    await ctx.message.delete()

@client.command(aliases=['sa'])
async def say(ctx, *, content):
    await ctx.send(f'{ctx.author.mention} sagt **{content}**\n')

@client.command(aliases=['googl'])
async def google(ctx, *args):
    msg = " ".join(args)
    await ctx.send(f"https://www.google.com/search?q={msg}")

@client.command(aliases= ['Rolle','Role'])
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, *, role: discord.Role):
        if member:
            if role:
                if not role in member.roles:
                    await member.add_roles(role, atomic=True)
                    await ctx.send(f'**{member}** hat die Rolle **{role.name}** erhalten.')
                elif role in member.roles:
                    await member.remove_roles(role, atomic=True)
                    await ctx.send(f'**{member}** wurde die Rolle **{role.name}** entfernt.')
            else:
                await ctx.send('Es konnte keine Rolle gefunden werden.')
        else:
            await ctx.send('Es konnte niemand gefunden werden.')

ssp = ['Schere', 'Stein', 'Papier']


@client.command(pass_context=True, aliases= ['SSP','SchereSteinPapier'])
async def ssp(ctx, arg1):
    y = random.choice(ssp)
    if arg1.lower() == 'schere':
        if y == 'Schere':
            await ctx.send('Unentschieden, meine Wahl: Schere')
        elif y == 'Stein':
            await ctx.send('Du hast Verloren, meine Wahl: Stein')
        elif y == 'Papier':
            await ctx.send('Du hast Gewonnen, meine Wahl: Papier')
    if arg1.lower() == 'stein':
        if y == 'Schere':
            await ctx.send('Du hast Gewonnen, meine Wahl: Schere')
        elif y == 'Stein':
            await ctx.send('Unentschieden, meine Wahl: Stein')
        elif y == 'Papier':
            await ctx.send('Du hast Verloren, meine Wahl: Papier')
    if arg1.lower() == 'papier':
        if y == 'Schere':
            await ctx.send('Du hast Verloren, meine Wahl: Schere')
        elif y == 'Stein':
            await ctx.send('Du hast Gewonnen, meine Wahl: Stein')
        elif y == 'Papier':
            await ctx.send('Unentschieden, meine Wahl: Papier')

@ssp.error
async def ssp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(',ssp\r\n-Schere\r\n-Stein\r\n-Papier')

@client.command()
async def FBI(ctx):
    await ctx.send('FBI OPEN UP!<a:FBI:714039598023442442>')
    await ctx.message.delete()

@client.command()
async def happy(ctx):

    glücklich = [f'{ctx.author.mention} ist glücklich<a:HappyHai:714386972654829638>',
                 f'{ctx.author.mention} ist happy<:happy:714387141748195378>', f'{ctx.author.mention} ist happy<a:HappySquirtle:714387020775948349>']

    await ctx.send(random.choice(glücklich))
    await ctx.message.delete()

@client.command()
async def bomb(ctx):
    await ctx.send(f"{ctx.author.mention} zündet eine Bombe <a:bombe:713738303915950180>")
    await ctx.message.delete()

@client.command(pass_context=True, aliases=['gm'])
async def morgen(ctx):
    await ctx.send(f"{ctx.author.mention} wünscht euch allen einen schönen guten Morgen🌥️")
    await ctx.message.delete()

@client.command(pass_context=True, aliases=['ga'])
async def abend(ctx):
    await ctx.send(f"{ctx.author.mention} wünscht euch allen einen schönen Abend🌙")
    await ctx.message.delete()

@client.command(pass_context=True, aliases= ['gn8'])
async def nacht(ctx):
    await ctx.send(f"{ctx.author.mention} wünscht euch allen eine gute Nacht.🌜Schlaft gut!😴")
    await ctx.message.delete()

@client.command(aliases= ['Kick'])
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Tschüss {member.mention}")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte einen User pingen!{ctx.author.mention}')

@client.command(aliases= ['Ban'])
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Tschüss {member.mention}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User und gebe den Grund für den Bann an!{ctx.author.mention}')

@client.command(aliases= ['Mute'])
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Bitte spezifiziere einen Member")
        return
    await member.add_roles(role)
    await ctx.send("Rolle wurde hinzugefügt!")

@client.command(aliases= ['Unmute'])
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Bitte spezifiziere einen Member")
        return
    await member.remove_roles(role)
    await ctx.send("Rolle wurde entfernt!")

@client.command(pass_context=True, aliases= ['Tschüss', 'tschüss', 'byebye'])
async def bye(ctx):
    verabschiedung = [f"{ctx.author.mention} muss sich verabschieden👋",
                      f"{ctx.author.mention} muss sich verabschieden<a:hallohund:713804833219674164>",
                      f"{ctx.author.mention} muss sich verabschieden<a:halloblue:713805320769765476>"]
    await ctx.send(random.choice(verabschiedung))
    await ctx.message.delete()

@client.command(pass_context=True)
async def dance(ctx):
    tanzen = [f"{ctx.author.mention} tanzt<a:squidward_dance:714036420288708638>",
                      f"{ctx.author.mention} schwingt seine Hüfte<a:squidward_dance:714036420288708638>",
                      f"{ctx.author.mention} schwingt seine Hüfte<a:Dance_knossi:714036346770948109>",
              f"{ctx.author.mention} schwingt seine Hüfte<a:sheep_dance:714036530062032976>",
              f"{ctx.author.mention} schwingt seine Hüfte<a:KakTusse:714036919830446100>",
              f"{ctx.author.mention} schwingt sein Tanzbein<a:Dance_knossi:714036346770948109>"]
    await ctx.send(random.choice(tanzen))
    await ctx.message.delete()

@client.command(pass_context=True, aliases= ['funny'])
async def haha(ctx):
    lachen = [f"{ctx.author.mention} lacht sich schlapp<a:lachbear2:714042098046730290>",
              f"{ctx.author.mention} lacht sich kaputt<:trymacsLachflash:714042140577103902>",
              f"{ctx.author.mention}lacht haha<a:lachbear1:714042036684193864>"]
    await ctx.send(random.choice(lachen))
    await ctx.message.delete()

@client.command(pass_context=True)
async def birb(ctx):
    gifs = ['https://api.alexflipnote.dev/birb/aszFKGE_p9s_birb.gif',
            'https://api.alexflipnote.dev/birb/9UCjK3RAfhY_birb.jpg',
            'https://api.alexflipnote.dev/birb/8BC7TngPIwo_birb.png',
            'https://api.alexflipnote.dev/birb/1rhQa7cKKgI_birb.jpg',
            'https://api.alexflipnote.dev/birb/eSdYTohpeQM_birb.jpg',
            'https://api.alexflipnote.dev/birb/DAeGsrmrQc8_birb.png',
            'https://api.alexflipnote.dev/birb/Umi29l8ks28_birb.jpg',
            'https://api.alexflipnote.dev/birb/fpWawh1NZfk_birb.jpg',
            'https://api.alexflipnote.dev/birb/MWzKd_7ZdhU_birb.jpg',
            'https://api.alexflipnote.dev/birb/ylpJxptlsV4_birb.png',
            'https://api.alexflipnote.dev/birb/39k4Km6dpJQ_birb.jpg',
            'https://api.alexflipnote.dev/birb/ZwmtklmADCI_birb.png',
            'https://api.alexflipnote.dev/birb/_lGrnMEvC1c_birb.jpg',
            'https://api.alexflipnote.dev/birb/3N7CZxf9RJs_birb.jpg',
            'https://api.alexflipnote.dev/birb/9iiGSamWmx8_birb.jpg',
            'https://api.alexflipnote.dev/birb/fXFpf3pi43w_birb.jpg',
            'https://api.alexflipnote.dev/birb/D_UMcTjBBcQ_birb.jpg',
            'https://api.alexflipnote.dev/birb/-yd3lmLeKxY_birb.jpg',
            'https://api.alexflipnote.dev/birb/3alnpPhi6Zs_birb.jpg',
            'https://api.alexflipnote.dev/birb/1Lr3r0FB-Bg_birb.jpg',
            'https://api.alexflipnote.dev/birb/lUcL5-Ztd2w_birb.jpg',
            'https://api.alexflipnote.dev/birb/AiIzdiDz_oE_birb.png',
            'https://api.alexflipnote.dev/birb/fHHGKugJYi8_birb.jpg',
            'https://api.alexflipnote.dev/birb/jH0SOtQEfNo_birb.jpg',
            'https://api.alexflipnote.dev/birb/-b6c_yFLqWc_birb.jpg']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(gifs)}')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def cry(ctx):
    heuel = [f'{ctx.author.mention} heult rum<:cryyyy:715254723543826512>', f'{ctx.author.mention} heult rum<a:PandaCryyy:715254768594976829>']
    await ctx.send(random.choice(heuel))
    await ctx.message.delete()

@client.command(pass_context=True)
async def smile(ctx):
    freude = ['https://cdn.weeb.sh/images/BytqEyKPZ.gif',
            'https://cdn.weeb.sh/images/B1lUN1tDb.gif',
            'https://cdn.weeb.sh/images/HyC_4ytD-.gif',
            'https://cdn.weeb.sh/images/B1-UN1KPb.gif',
             'https://cdn.weeb.sh/images/H1RXNJKPZ.gif',
             'https://cdn.weeb.sh/images/SJBYN1YwZ.gif',
             'https://cdn.weeb.sh/images/H1DfsgJ5-.gif',
              'https://cdn.weeb.sh/images/HJz44ytDW.gif',
              'https://cdn.weeb.sh/images/SJz_4JKvW.gif']
    embed = discord.Embed(title=f"{ctx.author} ist happy")
    embed.set_image(url=f'{random.choice(freude)}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(pass_context=True)
async def blush(ctx):
    erröten = ['https://cdn.weeb.sh/images/BkVOqsshZ.png',
            'https://cdn.weeb.sh/images/B1NWGUmvb.gif',
            'https://cdn.weeb.sh/images/S1uZMIXP-.gif',
            'https://cdn.weeb.sh/images/HklJGIXPW.gif',
             'https://cdn.weeb.sh/images/ryI1GLXDb.gif',
             'https://cdn.weeb.sh/images/rkXur1ncz.gif',
             'https://cdn.weeb.sh/images/rkYmGIXPb.gif',
              'https://cdn.weeb.sh/images/ByvffI7PZ.gif',
              'https://cdn.weeb.sh/images/Hk-Vz8QPb.gif']
    embed = discord.Embed(title=f"{ctx.author} errötet")
    embed.set_image(url=f'{random.choice(erröten)}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(pass_context=True)
async def kiss(ctx, Member: discord.Member):
    kuss = ['https://cdn.weeb.sh/images/ry9uXAFKb.gif',
            'https://cdn.weeb.sh/images/BJSdQRtFZ.gif',
            'https://cdn.weeb.sh/images/Sksk4l51z.gif',
            'https://cdn.weeb.sh/images/SJQRoTdDZ.gif']
    embed = discord.Embed(title=f"{ctx.author} küsst {Member.name} ")
    embed.set_image(url=f'{random.choice(kuss)}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User!{ctx.author.mention}')

@client.command(pass_context=True)
async def slap(ctx, Member: discord.Member):
    schlag = ['https://cdn.weeb.sh/images/BkxEo7ytDb.gif',
            'https://cdn.weeb.sh/images/HJKiX1tPW.gif',
            'https://cdn.weeb.sh/images/HyPjmytDW.gif',
            'https://cdn.weeb.sh/images/rJ52XyYD-.gif',
            'https://cdn.weeb.sh/images/SJdXoVguf.gif']
    embed = discord.Embed(title=f"{ctx.author} schlägt {Member.name} ")
    embed.set_image(url=f'{random.choice(schlag)}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User!{ctx.author.mention}')

@client.command(pass_context=True)
async def hug(ctx, Member: discord.Member):
    huge = ['https://cdn.weeb.sh/images/Sk2gmRZZG.gif',
            'https://cdn.weeb.sh/images/BkFnJsnA-.gif',
            'https://cdn.weeb.sh/images/Hk3ox0tYW.gif',
            'https://cdn.weeb.sh/images/HJU2OdmwW.gif',
            'https://cdn.weeb.sh/images/SywetdQvZ.gif']
    embed = discord.Embed(title=f"{ctx.author} umarmt {Member.name} ")
    embed.set_image(url=f'{random.choice(huge)}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User!{ctx.author.mention}')

@client.command(pass_context=True)
async def cat(ctx):
    katze = ['https://cdn.weeb.sh/images/SJZJ7qNEYG.jpeg',
             'https://cdn.weeb.sh/images/HyGpgc44tG.jpeg',
             'https://cdn.weeb.sh/images/B1b0e9VNtG.jpeg',
             'https://cdn.weeb.sh/images/B1-UAKVNYf.png',
             'https://cdn.weeb.sh/images/HJz6z94VYf.jpeg',
             'https://cdn.weeb.sh/images/rkZJ-qNVKf.jpeg',
             'https://cdn.weeb.sh/images/SJWofc44tz.jpeg',
             'https://cdn.weeb.sh/images/SylpFNVFM.jpeg',
             'https://cdn.weeb.sh/images/S1WIGqVEFM.jpeg',
             'https://cdn.weeb.sh/images/rJWTfqENKG.jpeg',
             'https://cdn.weeb.sh/images/S1py9NVtf.png',
             'https://cdn.weeb.sh/images/r1gxAtE4Fz.png',
             'https://cdn.weeb.sh/images/HkdaK4NKz.jpeg',
             'https://cdn.weeb.sh/images/ryqW9NVYG.jpeg',
             'https://cdn.weeb.sh/images/Hyz0e9VEKz.jpeg',
             'https://cdn.weeb.sh/images/HkxX9NVKz.jpeg',
             'https://cdn.weeb.sh/images/ryWCfq44tz.jpeg',
             'https://cdn.weeb.sh/images/rkm79V4Kz.jpeg',
             'https://cdn.weeb.sh/images/S1DpYVNFG.jpeg',
             'https://cdn.weeb.sh/images/B1ozc4EKf.jpeg',
             'https://cdn.weeb.sh/images/rkgfl9ENtG.jpeg',
             'https://cdn.weeb.sh/images/SkHpKENtG.jpeg',]
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(katze)}')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def dog(ctx):
    hund = ['https://cdn.weeb.sh/images/HJU0sE4tf.jpeg',
             'https://cdn.weeb.sh/images/SyLdjVVtz.gif',
             'https://cdn.weeb.sh/images/SkVxjV4Ff.jpeg',
             'https://cdn.weeb.sh/images/SkeTJhVEFf.jpeg',
             'https://cdn.weeb.sh/images/rJ3b2N4YM.jpeg',
             'https://cdn.weeb.sh/images/rklCJsE4YG.jpeg',
             'https://cdn.weeb.sh/images/S1jFhEVtf.jpeg',
             'https://cdn.weeb.sh/images/SJQo0oN4Kz.jpeg',
             'https://cdn.weeb.sh/images/Skl6CiVEKz.jpeg',
             'https://cdn.weeb.sh/images/B1bFAcVEFG.jpeg',
             'https://cdn.weeb.sh/images/rkbrlo4NKf.jpeg',
             'https://cdn.weeb.sh/images/BkGR7hNVKf.jpeg',
             'https://cdn.weeb.sh/images/H1bvJhNNtM.jpeg',
             'https://cdn.weeb.sh/images/BJYK2VNFf.gif',
             'https://cdn.weeb.sh/images/rJxRu2EVKf.jpeg',
             'https://cdn.weeb.sh/images/SysCsNNKz.jpeg',
             'https://cdn.weeb.sh/images/Skx2CoV4YG.jpeg',
             'https://cdn.weeb.sh/images/H1uniNVKz.gif',
             'https://cdn.weeb.sh/images/ryOyh4VYf.jpeg',
             'https://cdn.weeb.sh/images/Hke3_sVEYM.jpeg']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(hund)}')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def facts(ctx):
    fact = ['https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1518.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1519.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1520.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1521.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1522.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1523.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1524.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1525.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1526.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1527.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1528.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1529.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1530.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1531.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1532.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1533.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1534.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1535.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1536.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1537.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-51.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-53.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1737.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1738.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1739.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1740.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1741.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1742.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1743.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1744.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1745.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1746.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1747.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1337.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1338.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1339.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1340.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1341.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1342.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1343.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1344.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1345.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1346.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1347.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1348.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1349.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1350.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1351.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1352.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1353.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1354.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1355.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1356.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1748.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1749.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1750.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1751.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1752.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1753.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1754.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1755.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1756.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-55.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-56.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-57.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-58.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1478.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1479.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1480.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1481.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1482.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1483.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1484.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1485.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1486.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1488.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1487.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1489.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1490.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1491.jpg']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(fact)}')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def meme(ctx):
    memes = ['https://i.redd.it/jt3n1vpmqjz41.jpg',
             'https://i.redd.it/a9e0j64j2kz41.jpg',
             'https://i.redd.it/qvt6iwombjz41.jpg',
             'https://i.redd.it/lzzy74x31iz41.jpg',
             'https://i.redd.it/8ccxus9p2jz41.jpg',
             'https://i.redd.it/wlpmst4zhmz41.jpg',
             'https://i.redd.it/zuhb8y2fqiz41.jpg',
             'https://i.redd.it/i4pkozf2cmz41.jpg',
             'https://i.redd.it/zgshzlvjoiz41.png',
             'https://i.redd.it/gvn4qvhkskz41.jpg',
             'https://i.redd.it/rskxqjrlglz41.jpg',
             'https://i.redd.it/7vyos3gb8iz41.jpg',
             'https://i.redd.it/rvjum51kqhz41.jpg',
             'https://i.imgur.com/17DAtWh.jpg',
             'https://i.redd.it/0d2midft7iz41.png',
             'https://i.redd.it/t5ty7ysi7jz41.jpg',
             'https://i.redd.it/m7dkt2qqafz41.jpg',
             'https://i.redd.it/fq5fiaimrjz41.png',
             'https://i.redd.it/yftr8a8c5iz41.gif',
             'https://i.redd.it/dm5jxrg5ekz41.gif',
             'https://i.redd.it/1nwhtqi2kiz41.jpg',
             'https://i.redd.it/05z631u1uiz41.jpg',
             'https://i.redd.it/3xqovk6jriz41.jpg',
             'https://i.redd.it/rmtg1npuyfz41.jpg',
             'https://i.redd.it/w0jhmxh3siz41.jpg',
             'https://i.redd.it/sfemxc030jz41.jpg',
             'https://i.redd.it/nbwc886oofz41.jpg',
             'https://i.redd.it/bhivk1drkiz41.jpg',
             'https://i.redd.it/8zls0mszojz41.jpg',
             'https://i.redd.it/26h08uaixgz41.jpg',
             'https://i.redd.it/xkdi5ykpmhz41.gif',
             'https://i.redd.it/mw1q65me0kz41.jpg',
             'https://i.redd.it/1az4rcwmzfz41.jpg',
             'https://i.redd.it/mhhed5jxxgz41.jpg',
             'https://i.redd.it/vstog5gq0gz41.jpg',
             'https://i.redd.it/efjqs3n46jz41.png',
             'https://i.redd.it/imvl0ik0vhz41.jpg',
             'https://i.redd.it/mfb1hoa6cfz41.jpg',
             'https://i.redd.it/45cpalc5biz41.gif',
             'https://i.redd.it/zze7i8h5mgz41.jpg',
             'https://i.redd.it/pjqkgf39hfz41.png',
             'https://i.redd.it/ivordrzhniz41.jpg',
             'https://i.redd.it/0u4qv7xbpgz41.jpg',
             'https://i.redd.it/d7dy67287hz41.jpg',
             'https://i.redd.it/82b6esmrpkz41.jpg',
             'https://i.redd.it/t5lec9olthz41.jpg',
             'https://i.redd.it/fqtrm7559kz41.jpg',
             'https://i.redd.it/hmgrr26byiz41.jpg',
             'https://i.redd.it/3t73af0g0hz41.jpg',
             'https://i.redd.it/z4g3jtu8vfz41.jpg',
             'https://i.redd.it/gtuv5twr1hz41.png',
             'https://i.redd.it/uf5uefui1lz41.jpg',
             'https://i.redd.it/52ug91jczhz41.png',
             'https://i.redd.it/vz7w7m5hwfz41.jpg',
             'https://i.redd.it/osb5yj9l2hz41.png']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(memes)}')
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Angefordert von {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Servername", value=member.display_name)

    embed.add_field(name="Erstellt am:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Beigetreten am:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Rollen ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top Rollen:", value=member.top_role.mention)

    await ctx.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User!{ctx.author.mention}')

@client.command(aliases= ['Unban'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title=":white_check_mark:Der Bann wurde erfolgreich aufgehoben!", description=f"`{member}` wurde ungebannt!", color=discord.Color.green())
            await ctx.send(embed=embed)
            return

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, Frage):
    antworten = ['Ja.',
                 'Absolut!',
                 'Nein.',
                 'Vielleicht.',
                 'Absolut nicht!',
                 'Überhaupt nicht!',
                 'Das ist durchaus möglich.',
                 'Lieber nicht.',
                 'Das ist unmöglich!',
                 'Wahrscheinlich.',
                 'Sehr Wahrscheinlich.',
                 'Eventuell.',
                 'Sieht so aus.',
                 'Unwahrscheinlich.',
                 'Versuche es später noch einmal.']
    await ctx.send(f'Frage: {Frage}\nAntwort: {random.choice(antworten)}')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte stelle mir eine Frage!{ctx.author.mention}')

@client.command(aliases=['1&2'])
async def einsundzwei(ctx, *, Frage):
    Antworten = ['1','2']
    await ctx.send(f'Frage: {Frage}\nAntwort: {random.choice(Antworten)}')

@einsundzwei.error
async def einsundzwei_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Stelle mir bitte eine Frage!{ctx.author.mention}')

@client.command()
async def rolecolor(ctx, role: discord.Role, color: discord.Color):
    await role.edit(color=color)

@rolecolor.error
async def rolecolor_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge die **Rolle**, bei der du die Farbe ändern möchtest und nutzte bei deinem **Farbcode** `0x` statt `#`{ctx.author.mention}')

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member:
        embed = discord.Embed(title=f'Avatar von {member.name}', description=' ')
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'Avatar: {ctx.message.author.mention}', description=' ')
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User, um seinen Avatar angezeigt zu bekommen{ctx.author.mention}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count=2):
    if ctx.message.author.bot == False:
        deleted = await ctx.message.channel.purge(limit=count + 1)
        message = await ctx.message.channel.send(f"Es wurden {len(deleted) - 1} Nachricht(en) gelöscht!")
        await asyncio.sleep(3)
        await message.delete()

@client.command(pass_context=True)
async def createticket(ctx):
    guild = ctx.guild

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False,
                                                        read_message_history=False),  # Default Rolle
        guild.get_role(703198499688415312): discord.PermissionOverwrite(read_messages=True, send_messages=True,
                                                                        read_message_history=True),  # Team Rolle
        guild.get_member(ctx.author.id): discord.PermissionOverwrite(read_messages=True, send_messages=True,
                                                                     read_message_history=True)  # Ticket Owner
    }

    channel = await guild.create_text_channel(name=f"{ctx.author.name}`s-ticket", overwrites=overwrites)

    await ctx.send(f"Ticket erfolgreich erstellt. ( {channel.mention} )")
    await channel.send(f"{ctx.author.mention} braucht Hilfe!")

@client.command()
async def deleteticket(ctx):
    if "ticket" in ctx.channel.name:
        await ctx.channel.delete()




client.run('NzE1MTg0MTQzNzc1OTU3MDg0.Xs5hLQ.5Q7hwHOfCA24HB7_Iuwy79geaR4')