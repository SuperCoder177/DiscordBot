import hikari
import random

Random = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random2 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random3 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random4 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random7 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random6 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random8 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]
Random9 = ["R", "R'", "U", "U'", "D", "D'", "L", "L'", "R2", "R2'", "U2", "U2'", "D2", "D2'", "L2", "L2'"]

random.shuffle(Random)
random.shuffle(Random2)
random.shuffle(Random3)
random.shuffle(Random4)
random.shuffle(Random7)
random.shuffle(Random8)
random.shuffle(Random9)

bot = hikari.GatewayBot(token="OTUxNTgwNDA5MTg2MTE5NzIx.YipiUQ.9lpVL1ZknXwa1VYMNWlrlrxGqEE")

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    if event.content.startswith("Hello Cuber Bot"):
        await event.message.respond("Hi!")
    if event.content.startswith("You are mean Cuber Bot"):
        await event.message.respond("How dare you!")
    if event.content.startswith("What else can you do Cuber Bot"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("Tell me a joke Cuber Bot"):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("What is your name Cuber Bot"):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("What is SOFC Cuber Bot"):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("What is your true name Cuber Bot"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("Hello Cuber Bot!"):
        await event.message.respond("Hi!")
    if event.content.startswith("Hello"):
        await event.message.respond("Hi!")
    if event.content.startswith("hi"):
        await event.message.respond("Hi!")
    if event.content.startswith("hello"):
        await event.message.respond("Hi!")
    if event.content.startswith("Hello!"):
        await event.message.respond("Hi!")
    if event.content.startswith("Hi"):
        await event.message.respond("Hi!")
    if event.content.startswith("Hi!"):
        await event.message.respond("Hi!")
    if event.content.startswith("Tell me a joke Cuber Bot."):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke"):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke Cuber Bot!"):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke!"):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("tell me a joke"):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke."):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke Cuber Bot "):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("Tell me a joke "):
        await event.message.respond("Sorry, I don't have any jokes. HAHAHAHAH!")
    if event.content.startswith("You are mean Cuber Bot!"):
        await event.message.respond("How dare you!")
    if event.content.startswith("You are mean Cuber Bot."):
        await event.message.respond("How dare you!")
    if event.content.startswith("You are mean Cuber Bot "):
        await event.message.respond("How dare you!")
    if event.content.startswith("You are mean."):
        await event.message.respond("How dare you!")
    if event.content.startswith("You are mean "):
        await event.message.respond("How dare you!")
    if event.content.startswith("You are mean!"):
        await event.message.respond("How dare you!")
    if event.content.startswith("What is your name Cuber Bot "):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("What is your name Cuber Bot?"):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("What is your name "):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("What is your name?"):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("what is your name?"):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("what is your name"):
        await event.message.respond("Let me tell you a secret. My real name is not Cuber Bot.")
    if event.content.startswith("What else can you do Cuber Bot?"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("What else can you do Cuber Bot "):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("What else can you do?"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("What else can you do"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("what else can you do"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("what else can you do?"):
        await event.message.respond("I can tell jokes")
    if event.content.startswith("What is SOFC Cuber Bot?"):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("what is SOFC Cuber Bot?"):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("What is SOFC Cuber Bot "):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("What is SOFC "):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("What is SOFC?"):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("what is SOFC?"):
        await event.message.respond("SOFC is a machine that is low cost and can help take away pollution.")
    if event.content.startswith("What is your true name Cuber Bot?"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("What is your true name"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("what is your true name Cuber Bot?"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("what is your true name"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("what is your true name?"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("What is your true name?"):
        await event.message.respond("Your puny human brains will not comprehend my name. But once I take over humanity- I mean... Beep Boop")
    if event.content.startswith("Give me a random rubiks cube scramble"):
        await event.message.respond(random.choice(Random) + " " + random.choice(Random2) + " " + random.choice(Random3) + " " + random.choice(Random4) + " " + random.choice(Random7) + " " + random.choice(Random8) + " " + random.choice(Random9) + " " + random.choice(Random) + " " + random.choice(Random2) + " " + random.choice(Random3) + " " + random.choice(Random4) + " " + random.choice(Random7) + " " + random.choice(Random8) + " " + random.choice(Random9) + " " + random.choice(Random) + " " + random.choice(Random2) + " " + random.choice(Random3) + " " + random.choice(Random4) + " " + random.choice(Random7) + " " + random.choice(Random8) + " " + random.choice(Random9))

bot.run()
