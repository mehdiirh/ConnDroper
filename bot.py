'''
Writed By : t.me/iSANDSTORM
Channel: @MPrxy
'''


from telebot import TeleBot
from time import sleep
import os, schedule, requests

admin = [       # Enter ID of admin(s) here
    581171836,
    422072031
]

TOKEN = 'YOUR_TOKEN_GOES_HERE'     # Your Telegram TOKEN
sens = 600    # Sensitivity of connections number
timer = 300   # Set timer to DROP connections ( enter in Seconds )
port = 80     # Your proxy external port

bot = TeleBot(TOKEN)

bot.send_message(admin[0], f'- Sensivity has been set to: {sens}\n- Timer set to {timer} seconds')
print('HELLO !')


def send(admin, message):
    for i in admin:
        bot.send_message(i, message, parse_mode='markdown')


def do_block():
    idiots = str(os.popen(
        f"netstat -tn 2>/dev/null | grep :{port} | awk '{{print $5}}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read())

    idiots = idiots.split('\n')

    idis = []
    for i in idiots:
        if i == '':
            continue
        i = i.split()
        i = tuple(i)
        idis.append(i)

    txt1 = '*RESULT :* \n\n'
    for conn, ip in idis:
        conn = int(conn)
        if conn > sens:
            response = os.system(f"iptables -A INPUT -s {ip} -j DROP")
            if response == 0:
                txt1 += f'`{ip}` ({conn}) *DROPED* !\n'

                try:
                    with open('BLOCKED.txt', 'a') as file:
                        file.write(f'\n{ip}')
                except:
                    pass

                print(f'{ip} ({conn}) DROPED !')

            else:
                txt1 += f'`{ip}` ({conn}) FAILED TO DROP !'
            sleep(0.3)
        else:
            txt1 += f'`{ip}` ({conn}) *NOT FLOODER* !\n'

    send(admin, txt1)


do_block()
schedule.every(timer).seconds.do(do_block)

while True:
    schedule.run_pending()
    sleep(1)
