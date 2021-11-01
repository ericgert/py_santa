import yagmail 
import configparser
import random

#grab the creds from the config file
config = configparser.ConfigParser()
config.read('../santa.ini')
mail_user = config['SANTA_MAIL']['user']
mail_password = config['SANTA_MAIL']['password']

fam_list = [
    ('Eric',{
    "email":"eric.gert@gmail.com"
    ,"exclusions":["Eric","Brette","Troy"]
    })
    , ('Brette',{
        "email":"gertonson.brette@gmail.com"
        , "exclusions":["Brette","Eric","Christi"]
    })
    , ('Steve',{
        "email":"sfgert@gmail.com"
        , "exclusions":["Steve","Marti","Eric"]
    })
    , ('Marti',{
        "email":"mpgert1@gmail.com"
        , "exclusions":["Marti","Steve","Elizabeth Lee"]
    })
    , ('Christi',{
        "email":"wheatonc@dtccom.net"
        , "exclusions":["Christi","Troy","Steve"]
    })
    , ('Troy', {
        "email":"wheaton@dtccom.net"
        , "exclusions":["Troy","Christi","Matt"]
    })
    , ('Matt', {
        "email":"gertonson@hotmail.com"
        , "exclusions":["Matt","Elizabeth Lee","Marti"]
    })
    , ('Elizabeth Lee', {
        "email":"eleetark@gmail.com"
        , "exclusions":["Elizabeth Lee","Matt", "Brette"]
    })
]

#create list of just the names left to be drawn (all names initially)
santas = [i[0] for i in fam_list]
gifted = [i[0] for i in fam_list]
full_name_list = [i[0] for i in fam_list]
pair_list = []

for _ in range(len(full_name_list)):

    name_num = random.randint(0,len(santas)-1)
    name = santas[name_num]
    fam_index = full_name_list.index(name)
    email = fam_list[fam_index][1]['email']
    exclusions = fam_list[fam_index][1]['exclusions']

    while True:
        pick_num = random.randint(0,len(gifted)-1)
        pick = gifted[pick_num]
        if pick not in exclusions:
            break
    
    

    print('Sending email to {}.'.format(name))
    message_body = """ Hi {},

    Your Secret Santa draw is {}.  Merry Christmas!  Enjoy this wonderful season as we celebrate the birth of our Savior Jesus Christ!

    Sincerely,

    Santa Gert
    """.format(name, pick)
    yag = yagmail.SMTP(user=mail_user, password=mail_password)
    yag.send(
        to = email, 
        subject = 'Secret Santa Assignment',
        contents = message_body)
    
    santas.pop(name_num)
    gifted.pop(pick_num)

    import time
    time.sleep(5)



#test email
# try:
#     yag = yagmail.SMTP(user=mail_user, password=mail_password)

#     yag.send(to='eric.gert@gmail.com'
#     , subject='Test from Santa'
#     , contents='Yagmail test email for you brother man.')
#     print("check yo mail sucker")
# except:
#     print("that didnt work brother man")
#     raise
