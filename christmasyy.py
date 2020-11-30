import discord
import json
from discord.ext import commands
client = commands.Bot(command_prefix="*")

@client.event
async def on_ready():
    general_channel = client.get_channel(720071120291758093)
    await general_channel.send('Ho Ho Ho, Merry Christmasssss https://cache.lovethispic.com/uploaded_images/291344-Ho-Ho-Ho...merry-Christmas.jpg')

@client.event
async def on_message(message):

    if message.content == '*':
        general_channel = client.get_channel(720071120291758093)
        myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0 beta", color=0xf80000)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="not applicable",inline=False)        
        myEmbed.set_footer(text="Developed by Exploit#0001")

        
        await general_channel.send(embed=myEmbed)

    if message.content == '*help':
        general_channel = client.get_channel(720071120291758093)
        myEmbed1 = discord.Embed(title="Help", description="List of helpful commands and support contacts for the developer(s)",color=0xf80000 )
        myEmbed1.add_field(name="Commands", value="*christmaslist, *mistletoe, *christmasday, *cookies, *presents, *chimney, *caroline, *gift (run *gift for more)", inline=False)
        myEmbed1.add_field(name="More Support:", value="Contact exploit#0001 with bug reports", inline=False)
        myEmbed1.set_footer(text="Developed by exploit#0001")

        await general_channel.send(embed=myEmbed1)
    
    if message.content =='*gift':
        general_channel = client.get_channel(720071120291758093)
        myEmbed2 = discord.Embed(title="*gift commands", description="List of Avaliable commands for gift(Syntax: *gift (item) please)", color=0xf80000 )
        myEmbed2.add_field(name="Commands",value="*gift lamborghini, *gift adidas, *gift candy cane, *gift teddy bear, *gift iphone, *gift gingerbread house, *gift bells",inline=False)
        myEmbed2.add_field(name="More Support:", value="Contact exploit#0001 with bug reports", inline=False)
        myEmbed2.set_footer(text="Developed by exploit#0001")

        await general_channel.send(embed=myEmbed2)



    
    if message.content == '*christmaslist':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('I want: Toys, a hot girl and, good grades for once')
    
    if message.content == 'Merry Christmas':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('Merry Christmas :)))) https://tenor.com/pa09.gif')

    if message.content == 'merry christmas':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('Merry Christmas :)))) https://tenor.com/pa09.gif')
    
    if message.content == 'hi':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('How are you :)')
    
    if message.content == 'good':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("That's Great to Hear :))) https://tenor.com/0BBv.gif")

    if message.content == 'how about you':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("I'm fantastic; So excited for Christmas :))) Thanks for asking! https://tenor.com/W9iz.gif")

    if message.content == 'how about you?':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("I'm fantastic; So excited for Christmas :))) Thanks for asking! https://tenor.com/W9iz.gif")
    
    if message.content == 'how are you':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("I'm fantastic; So excited for Christmas :))) Thanks for asking! https://tenor.com/W9iz.gif")
    
    if message.content == 'how are you?':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("I'm fantastic; So excited for Christmas :))) Thanks for asking! https://tenor.com/W9iz.gif")

    if message.content == '*mistletoe':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('Aw is that for me???  https://tenor.com/EGsT.gif')

    if message.content == '*christmasday':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('The Day of Christmas is The 25th of December of 2020')

    if message.content == '*cookies':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('Here are some cookies and warm milk :)  https://www.history.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_620/MTU3ODc4Njg1MTIyMjQxODY1/image-placeholder-title.webp ' )
    
    if message.content == '*presents':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("Here's a present :) https://hallmark.brightspotcdn.com/36/33/e1782a88b046aaefd6a989cebd2c/digi17-overlay-theperfectchristmaspresent-853x570f.jpg ")
    
    if message.content == '*chimney':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("Santa is slowly creeping down your chimney https://images2.minutemediacdn.com/image/upload/c_crop,h_1125,w_2000,x_0,y_99/f_auto,q_auto,w_1100/v1554992339/shape/mentalfloss/90217-istock-487636772_0.jpg")
       
    if message.content == '*caroline':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("Here is some caroling https://media.giphy.com/media/3o7TKp0DGvFyYeSxwc/giphy.gif")
    
    if message.content == '*gift lamborghini please':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("Here is a Lambo :) Thanks for asking :) https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2020-lamborghini-aventador-svj-roadster-drive-107-1576871367.jpg?crop=0.796xw:0.673xh;0.176xw,0.327xh&resize=2048:*")
    
    if message.content == '*gift adidas please':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send('Here are some Adidas Shoes :) Thanks for asking :) https://media.discordapp.net/attachments/720071120291758093/782564971221090325/IMG_20201129_164333.jpg')

    if message.content == '*gift candy cane please':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("Here are some Candy Canes :) Thanks for asking :) https://www.thespruceeats.com/thmb/L3DiFopwvIgHFVRcW6MblHILAqw=/3264x3264/smart/filters:no_upscale()/candy-canes-and-christmas-lights-159084144-59e663750d327a00108af168.jpg")
 
    if message.content =='*gift iphone please':
            general_channel = client.get_channel (720071120291758093)
            await general_channel.send("Here is an Iphone for you :) Thanks for asking https://www.apple.com/newsroom/images/product/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.medium.jpg")

    if message.content == '*gift teddy bear please':
        general_channel = client.get_channel (720071120291758093)
        await general_channel.send("Here is a Teddy Bear for you :) Thanks for asking https://www.melijoe.com/images/142519/open_graph.jpg")

    if message.content == '*gift gingerbread house please*':
        general_channel = client.get_channel (720071120291758093)
        await general_channel.send("Here is a Little GingerBread House made by Gingie herself :)https://sugarandcharm.com/wp-content/uploads/2019/12/gingerbread-house-_-41.jpg")
    
    if message.content == '*gift bells please':
        general_channel = client.get_channel (720071120291758093)
        await general_channel.send("Here are some shiny bells :)))")
    
    if message.content == '*gift lamborghini':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking?  https://tenor.com/F72M.gif")
    
    if message.content == '*gift adidas':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking? https://tenor.com/F72M.gif")
    
    if message.content == '*gift candy cane':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking? :CBI_koolkid_dance:  https://tenor.com/F72M.gif")

    if message.content == '*gift teddy bear':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking? :CBI_koolkid_dance:  https://tenor.com/F72M.gif")

    if message.content == '*gift iphone':
        general_channel = client.get_channel(720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking? :CBI_koolkid_dance:  https://tenor.com/F72M.gif")
    
    if message.content == '*gift gingerbread house':
        general_channel = client.get_channel (720071120291758093)
        await general_channel.send("What's the magic word??? Do you want coal in your stocking? :CBI_koolkid_dance:  https://tenor.com/F72M.gif")
    await client.process_commands(message)


@client.command()
async def gift(ctx, gift, target, keyword=None):
    if keyword != "please":
        print("say something about needing to say please")
        return
    
    dict_gifts = {
        "gingerbreadhouse": "gifted a gingerbread house made by gingie hehe https://bit.ly/39qI4dm ",
        "pants": "gifted some pants",
        "lamborghini": "https://bit.ly/36gn8nl gifted a lamborghini",
        "candycane": "gifted a candy cane",
        "mistletoe": "gifted a kiss under the mistletoe https://tenor.com/EGsT.gif",
        "adidas": "gifted some fresh adidas https://bit.ly/3qbWiom",
        "bells": "gifted some shiny bells https://tenor.com/2Dxp.gif",
        "cookies": "gift some delicous cookies"}

    finalstr = "" 

    for key, values in dict_gifts.items():
         finalstr = f"{finalstr}, {key}"
    await ctx.send(finalstr)

    await ctx.send( f"{ctx.message.author.mention} {dict_gifts[gift]} to {target}") 

    with open("data.json", "r") as f:
         content = json.load(f)
         f.close()

    if ctx.message.author.name not in content:
        content[ctx.message.author.name] = gift
    else:
        content[ctx.message.author.name] = f"{content[ctx.message.author.name]}, {gift}"

    with open("data.json", "w") as f:
        json.dump(content, f, indent=4)
        f.close()
        
# with open("somefilename.txt", "r") as f:
    #     content = f.readlines()
    #     f.close()
    # stats = {}
    # for item in content:
    #     name = item.split(":")[0]
    #     print(item.split(":")[1])
    #     received_gifts = item.split(":")[1].split(",")
    #     stats[name] = received_gifts

    # if target not in stats:
    #     stats[target] = gift
    # else:
    #     stats[target].append(gift)

    # with open("somefilename.txt", "w") as f:
    #     f.truncate(0)
    #     for key, values in stats.items():
    #         # print(values)
    #         values = ','.join(values)
    #         f.write(f"{key}:{values}")
    #         f.write("\n")

    #     f.close()




@client.event
async def on_member_join(member):
        Welcome_channel = client.get_channel(720071120291758093)
        await Welcome_channel.send("Ho Ho Ho Merry Christmas")

@client.event
async def on_member_leave(member):
        Welcome_channel = client.get_channel(720071120291758093)
        await Welcome_channel.send("You're Going to Get Coal in Your Stocking on Christmas")


@client.event
async def on_disconnect():
    general_channel = client.get_channel(720071120291758093)
    await general_channel.send('Are you done with your work yet? Yea I didnt think so, so get back to work')
#Run the client on the server
client.run('NzgyNDkwOTE1OTUxMzQ1Njc1.X8M9dA.MvG4R-SWwKBAdv9gdjtA_4NovxE')
