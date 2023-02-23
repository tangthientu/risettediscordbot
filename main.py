import discord
import random
import requests
import joke_api
import json
from discord.ext import commands
intents = discord.Intents.default()
intents = discord.Intents.all()
client = discord.Client(intents=intents)



#inspire
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
#jokes
URL = 'https://official-joke-api.appspot.com/random_joke'


def __check_valid_response_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_joke():
    request = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = __check_valid_response_code(request)

    return data

#Channel ID
announcement=(1065894318725922826)
#role id
roleid=(336089436938829834)
#lines
hello_line = ["Hello senpai.", "Happy to see you senpai.", "Senpai!","Hello there handsome."]
love_line = ["I love you too senpai...","Um glad you said it senpai.","Risette love you too.","You... you really mean it senpai?","Im lucky to have you by my side senpai"]
bye_line =["Aww.. see you later senpai!","Do you have to go senpai..","Okay i see you later senpai.","We will talk later then senpai.","Alright i see you around senpai.","Can you please stay for just a bit longer."]
morning_line=["Good morning senpai!","Good morning handsome."]
night_line=["Good night senpai.","Have a sweet dream senpai.","I hope you will dream of me senpai"]
goodsong_line=["Nice choice senpai","Ohhh this one is perfect","Do you want Risette to sing this song for you senpai."]
badsong_line=["Really? right in front me senpai?","Im covering my ear!!","You have such a bad taste senpai","That's it, Risette is leaving.","This song is bad and you know it right senpai?","You are fucking **cringe** senpai"]
binz_line=["How **disgusting**","Did you read the rules for this server senpai. No binz is allowed.","Ewwww!! really?","Please senpai, please don't play any binz song","I fucking hate you senpai","I guess you are not really my senpai after all.."]
ngot_line=["You are such a _kẹo con_ senpai","_Lần cuối đi bên nhau_ moment"]
cursed_line=["Language!!","Rude.","||Mày chửi thề con cặc, nói chuyện vô văn hóa||"]
rating_line=["Cringe","not cringe"]
coin_line=["Head!","Tail!"]

#keywords
hi_keywords=["hello","hi"]
bye_keywords=["bye","goodbye","see you"]
love_keywords=["like","love"]
morning_keywords=["good morning"]
night_keywords=["good night","sweet dream"," go to sleep"]
credit_keywords=["made","make","created","credit","programed","your parent","your father","your mother"]
gift_keywords=["something","give","present","gift"]
goodsong_kw=["Persona","Daftpunk","Cyberpunk","Weeknd","TUYU","SAMURAI","Evangelion"]
badsong_kw=["Huỳnh James","pjnboy","travis scott","Đạt g","rồi tới luôn","roi toi luon","Dance monkey"]
binz_kw=["binz"]
ngot_kw=["ngọt","ngot","thắng","lan cuoi","chuyen kenh","em dao nay"]
rating_kw=["cringe","kek"]
rise=["rise","risette"]
cursed_kw=["fuck","địt","đụ","djt","lone","loz","đĩ","đỉ","fak","fuk","lồn"]
music=["play","+play","/play",".play","-play","_play","p","+p","/p",".p","-p","_p","View on vexera.io","Added to ProQueue"]
gifts=["Muscle Drink","Medicine","Bead Chain","Life Stone","Kanji's Homemade doll","Nanako's Chocolate","Risette's Pudding","DR.Salt NEO","Second Maid","The Natural","TaP Soda","Soul Drop","Snuff Soul","Soul Food","Super Croquette"]
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
#hello line
  if any(word in message.content.lower() for word in hi_keywords) and any(word in message.content.lower() for word in rise) :
    await message.channel.send(random.choice(hello_line))
#inspire
  if message.content.lower().startswith('inspire me rise'):
    quote = get_quote()
    await message.channel.send(quote)
#joke
  if message.content.lower().startswith('tell me a joke rise'):
    joke = get_joke()
    print(joke)
    await message.channel.send(joke['setup'] + '\n' + joke['punchline'])
        
#good bye line
  if any(x in message.content.lower() for x in bye_keywords) and any(x in message.content.lower() for x in rise) :
    await message.channel.send(random.choice(hello_line))


#love line
  if any(x in message.content.lower() for x in love_keywords) and any(x in message.content.lower() for x in rise) :
    await message.channel.send(random.choice(love_line))
#morning line
  if any(x in message.content.lower() for x in morning_keywords) and any(x in message.content.lower() for x in rise) :
    await message.channel.send(random.choice(morning_line))
#night line
  if any(x in message.content.lower() for x in night_keywords) and any(x in message.content.lower() for x in rise) :
    await message.channel.send(random.choice(night_line))
#credit line

  if any(x in message.content.lower() for x in credit_keywords) and any(x in message.content.lower() for x in rise) :
    myid = '<@224012106721132544>'
    await message.channel.send('%s senpai programed me ! ' % myid)
#goodsong line 
  if any(x in message.content.lower() for x in goodsong_kw) and any(x in message.content.lower() for x in music) :
    await message.channel.send(random.choice(goodsong_line))
#badsong line 
  if any(x in message.content.lower() for x in badsong_kw) and any(x in message.content.lower() for x in music) :
    await message.channel.send(random.choice(badsong_line))
#binzsong line 
  if any(x in message.content.lower() for x in binz_kw)  :
    await message.channel.send(random.choice(binz_line))
#ngot song line 
  if any(x in message.content.lower() for x in ngot_kw) and any(x in message.content.lower() for x in music) :
    await message.channel.send(random.choice(ngot_line))
#cursed line
  if any(x in message.content.lower() for x in cursed_kw):
    await message.channel.send(random.choice(cursed_line))
#rating linee
  if any(x in message.content.lower() for x in rating_kw) and any(x in message.content.lower() for x in rise) :
    await message.channel.send(random.choice(rating_line))
#coin line
  if message.content.lower().startswith('flip a coin rise'):
    await message.channel.send(random.choice(coin_line))

#gift line
  if any(x in message.content.lower() for x in gift_keywords) and any(x in message.content.lower() for x in rise) :
    await message.channel.send('I want you to have this senpai  '+'\n **>  You received _%s_ from _Rise_ **' %random.choice(gifts))
# welcome member

@client.event
async def on_member_join(member):
  myid = '<@224012106721132544>'
  await client.get_channel(announcement).send(f"{member.name}({member.mention}) senpai has joined. Welcomeeee!! 🥰 "+' i will notify %s senpai about your arrival.' %myid)
  default_role = discord.utils.get(member.guild.roles, id=roleid)
  await member.add_roles(default_role)   
  
# goodbye member
@client.event
async def on_member_remove(any):
  myid = '<@224012106721132544>'
  await client.get_channel(announcement).send(f"{any.name}({any.mention}) senpai has left. Goodbye 😭"+' i will notify %s senpai about your departure.' %myid)
async def on_member_ban(user):
 
  await client.get_channel(announcement).send(f"{user.mention} senpai has been kicked. Congratulation you deserve it 😈")
 


client.run(
  'MTA2NTMwNDYyNzk3ODk4MTQ2OQ.GggNTB.ftMGz3IC6RKBGHo4dfJuazFLGy-O59P6abGiWE')
