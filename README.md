# ConnDroper
A bot for Block DDoS Attackers of MTProto Proxies


## Installation
### THIS installation just works on CentOS:

first of all you've to install git on your server:
```bash
yum install git -y
```

then, use this command to clone project into your server:
```bash
git clone https://github.com/mehdiirh/ConnDroper.git && cd ConnDroper/
```

#### edit file ```bot.py``` lines 5 - 13:
```python
admin = [       # Enter ID of admin(s) here
    581171836,
    422072031
]

TOKEN = 'YOUR_TOKEN_GOES_HERE'     # Your Telegram TOKEN
sens = 600    # Sensitivity of connections number
timer = 300   # Set timer to DROP connections ( enter in Seconds )
port = 80     # Your proxy external port
```


chmod installer:
```bash
chmod +x drp
```

run installer using this command:
```bash
./drp
```

Enter *1* and installing will started, after installation, bot will be run automatically


## Run Bot Manually later:

#### For running bot after installation, if bot goes off or crashed or etc. :
```bash
cd ConnDroper/
screen -S DROPER python3.6 bot.py
```

# GOOD LUCK ! ~ @iSANDSTORM
