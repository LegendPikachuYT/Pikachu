import sys
import time
import subprocess
import os
from pyfiglet import Figlet
from termcolor import colored
#code begins
os.system('clear')
print(colored('''
██████╗░██╗██╗░░██╗░█████╗░
██╔══██╗██║██║░██╔╝██╔══██╗
██████╔╝██║█████═╝░███████║
██╔═══╝░██║██╔═██╗░██╔══██║
██║░░░░░██║██║░╚██╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░██╗██╗░░░██╗███╗░░██╗████████╗
██║░░██║██║░░░██║████╗░██║╚══██╔══╝
███████║██║░░░██║██╔██╗██║░░░██║░░░
██╔══██║██║░░░██║██║╚████║░░░██║░░░
██║░░██║╚██████╔╝██║░╚███║░░░██║░░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░
''',color = 'blue'))
print("\n\n\n")
msg0=(colored('''+----------------------------------------------+
| Name:        Pikachu Hunter
| Author:      @LegendPikachu_YT
+----------------------------------------------+\n''',color = 'red'))
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
a = input("\n\nARE YOU SURE YOU WANT TO START (y/n) = ").lower()
if a == "y":
	msg1=(colored('''\n\n\n>>> PIKACHU HUNTER IS STARTING...>>>''',color = 'green'))
	for i in msg1:
        	sys.stdout.write(i)
        	sys.stdout.flush()
        	time.sleep(0.04)
	f = Figlet(font='5lineoblique')
	print(colored(f.renderText('PokeBall'),color = 'magenta'))
	print("\n\n")
	print(colored("#NOTE - YOUR ACCESS KEY IS = PIKA",color = 'red'))
	b = input("\n\nEnter Your Access Key Here (Must Be In Capital Letters) = ")
	if b == "PIKA":
		os.system('clear')
		z = Figlet(font='5lineoblique')
		print(colored(z.renderText('PIKACHU'),color = 'magenta'))
		print(colored("\n\n#NOTE - THIS TOOL SHOULD NOT BE USED FOR ANY ILLEGAL USE \n WE ARE NOT RESPONSIBLE IF YOU USE THIS TOOL\n FOR ANY ILLEGAL USE",color = 'red'))
		print(colored("\n\n>>> Opening The Tool Menu >>>",color = 'green'))
		print("\n\n")
		print(colored(''' ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ''',color = 'cyan'))
		print("\n\n")
		ae = Figlet(font='5lineoblique')
		print(colored(ae.renderText('MENU'),color = 'green'))
		print("\n\n")
		print(colored('''
		[01] HiddenEye		[02] Nmap 
		[03] Tbomb		[04] Phoneinfoga 
		[05] PhoneInfo		[06] Anon-SMS 
		[07] CamPhish		[08] SayCheese 
		[09] shark		[10] Zphisher 
		[11] sqlmap		[12] RED_HAWK 
		[13] Auto-Deface	[14] AOXdeface 
		[15] DDOS-ATTACK	[16] deface 
		[17] FotoSploit		[18] Metasploit 
		[19] Kali-NetHunter	[20] ADV PHISH 
		[21] Haxrat		[22] Termux Black 
		[23] CCTV-HACK		[24] Evil-Eye-Banner 
		[25] Extra Termux Keys	[26] Ghost-Droid 
		[27] BlackMafia		[28] Fsociety 
		[29] Sherlock		[30] Httrack 
		[31] CMS MAP		[32] TERMUX WEB KIT 
		[33] D-TECT		[34] WPSeku 
		[35] M-Dork		[36] Hash Cracker 
		[37] Sql Injection	[38] Dark-FLY 
		[39] Credmap		[40] Phonesploit 
		[41] Infect		[42] Pattern Lock Phish 
		[43] Parrot-OS-Shell	[44] NexPhish 
		[45] TelegramUser Adder [46] Lazymux 
		[47] ReconDog		[48] Wireshark
		[49] T-Load		[50] Termux -ApkTool 
		[51] Madcam		[52] Nano-Tool Maker 
		[53] About US		[54] Exit''',color = 'cyan'))
		print("\n\n")
		print(colored(''' ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ''',color = 'cyan'))
		print("\n\n")
		d = colored("Please Choose an Option From The Above List = ",color = 'red')
		c = int(input(d))
		if c == int(1):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python php curl openssh grep -y',shell = True)
			subprocess.call('git clone https://github.com/DarkSecDevelopers/HiddenEye.git && chmod 777 HiddenEye',shell = True)
			os.chdir('/data/data/com.termux/files/home/HiddenEye')
			subprocess.call('pip install -r requirements.txt',shell = True)
			subprocess.call('pip install requests && pip install pyngrok',shell = True)
			subprocess.call('pip install pgrep',shell = True)
			print(colored("[+] Hidden Eye Was Successfully Installed",color = 'green'))
			subprocess.call('python HiddenEye.py',shell = True)
		if c == int(2):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install nmap -y',shell = True)
			print(colored("[+] Successfully Installed Nmap",color = 'green'))
		if c == int(3):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python -y',shell = True)
			subprocess.call('git clone https://github.com/TheSpeedX/TBomb.git',shell = True)
			os.chdir('/data/data/com.termux/files/home/TBomb')
			print(colored("[+] Successfully Installed TBomb",color = 'green'))
			subprocess.call('bash TBomb.sh',shell = True)
		if c == int(4):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python python2 git -y',shell = True)
			subprocess.call('git clone https://github.com/abhinavkavuri/PhoneInfoga',shell = True)
			os.chdir('/data/data/com.termux/files/home/PhoneInfoga')
			subprocess.call('mv config.example.py config.py && python3 -m pip install -r requirements.txt',shell = True)
			subprocess.call('chmod +x phoneinfoga.py',shell = True)
			print(colored("[+] PhoneInfoga was Successfully Installed",color = 'green'))
			se = int(input("Enter Phone No. (with country code) = "))
			se2 = "python3 phoneinfoga.py -n " + str(se)
			print(colored("Copy Paste This Command --> "+"cd PhoneInfoga && "+ (se2)))
		if c == int(5):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python git -y',shell = True)
			subprocess.call('pip3 install termcolor && pip3 install pyfiglet && pip3 install phonenumbers && pip3 install sys',shell = True)
			subprocess.call('git clone https://github.com/LegendPikachuYT/Phoneinfo',shell = True)
			os.chdir('/data/data/com.termux/files/home/Phoneinfo')
			print(colored("[+] Successfully Installed Phoneinfo ",color = 'green'))
			subprocess.call('python3 phoneinfo.py',shell = True)
		if c == int(6):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python -y',shell = True)
			subprocess.call('git clone https://github.com/HACK3RY2J/Anon-SMS.git')
			print(colored('[+] Successfully Installed Anon-SMS',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/Anon-SMS')
			subprocess.call('sudo bash Run.sh',shell = True)
		if c == int(7):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git wget python python2 php -y',shell = True)
			subprocess.call('git clone https://github.com/techchipnet/CamPhish',shell = True)
			os.chdir('/data/data/com.termux/files/home/CamPhish')
			print(colored("[+] Successfully Installed CamPhish",color = 'green'))
			subprocess.call('chmod 777 camphish.sh && bash camphish.sh',shell = True)
		if c == int(8):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install php wget git httrack -y',shell = True)
			subprocess.call('git clone https://github.com/TechnicalHeadquarter/saycheese',shell = True)
			os.chdir('/data/data/com.termux/files/home/saycheese')
			print(colored("[+] Successfully Installed saycheese",color = 'green'))
			print(colored("Please Turn On Your Hotspot",color = 'red'))
			subprocess.call('chmod +x saycheese.sh && bash saycheese.sh',shell = True)
		if c == int(9):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg update && pkg upgrade && pkg install git -y',shell = True)
			subprocess.call('git clone https://github.com/Bhaviktutorials/shark',shell = True)
			print(colored("[+] Successfully Installed shark",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/shark')
			subprocess.call('chmod +x * && ./setup',shell = True)
			subprocess.call('shark',shell = True)
		if c == int(10):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git wget php curl -y',shell = True)
			subprocess.call('git clone git://github.com/htr-tech/zphisher.git',shell = True)
			print(colored("[+] Successfully Installed zphisher",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/zphisher')
			subprocess.call('bash zphisher.sh',shell = True)
		if c == int(11):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python python2 -y',shell = True)
			subprocess.call('git clone https://github.com/sqlmapproject/sqlmap',shell = True)
			os.chdir('/data/data/com.termux/files/home/sqlmap')
			print(colored("[+] Successfully Installed sqlmap",color = 'green'))
			subprocess.call('python2 sqlmap.py',shell = True)
		if c == int(12):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git php -y',shell = True)
			subprocess.call('git clone https://github.com/Tuhinshubhra/RED_HAWK',shell = True)
			os.chdir('/data/data/com.termux/files/home/RED_HAWK')
			print(colored("[+] Red Hawk was Successfully Installed",color = 'green'))
			subprocess.call('php rhawk.php',shell = True)
		if c == int(13):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			subprocess.call('pip2 install requests mechanize',shell = True)
			subprocess.call('git clone https://github.com/MRX-F4T4H-ID/Auto-Deface',shell = True)
			os.chdir('/data/data/com.termux/files/home/Auto-Deface')
			print(colored("[+] Auto-Deface was Successfully Installed ",color = 'green'))
			subprocess.call('python2 auto-deface.py',shell = True)
		if c == int(14):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			subprocess.call('git clone https://github.com/Ranginang67/AOXdeface',shell = True)
			os.chdir('/data/data/com.termux/files/home/AOXdeface')
			print(colored("[+] Successfully Installed AOXDeface ",color = 'green'))
			subprocess.call('python2 aox.py',shell = True)
		if c == int(15):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python2 figlet -y',shell = True)
			subprocess.call('git clone https://github.com/sikhoethicalhacking1/DDOS-ATTACK',shell = True)
			os.chdir('/data/data/com.termux/files/home/DDOS-ATTACK')
			print(colored("[+] Succefully Installed DDOS-ATTACK",color = 'green'))
			subprocess.call('chmod +x ddos.py && python2 ddos.py')
		if c == int(16):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			subprocess.call('pip2 install requests',shell = True)
			subprocess.call('git clone https://github.com/B012ED/deface.git',shell = True)
			os.chdir('/data/data/com.termux/files/home/deface')
			print(colored('[+]SucessFully Installed deface',color = 'green'))
			subprocess.call('python def.py',shell = True)
		if c == int(17):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install php python2 git -y',shell = True)
			subprocess.call('git clone https://github.com/Cesar-Hack-Gray/FotoSploit',shell = True)
			os.chdir('/data/data/com.termux/files/home/FotoSploit')
			print(colored('[+] Successfully Installed FotoSploit',color = 'green'))
			subprocess.call('bash install.sh --install --premium',shell = True)
			os.chdir('/data/data/com.termux/files/home/FotoSploit')
			subprocess.call('bash FotoSploit && show options',shell = True)
		if c == int(18):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python',shell = True)
			subprocess.call('pkg install php',shell = True)
			subprocess.call('pkg install ruby2',shell = True)
			subprocess.call('pkg install wget',shell = True)
			subprocess.call('apt gem install bundler',shell = True)
			subprocess.call('wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh',shell = True)
			subprocess.call('chmod +x metasploit.sh && ./metasploit.sh',shell = True)
			print(colored('[+] Successfully Installed Metasploit-framework',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/metasploit-framework')
			subprocess.call('msfconsole',shell = True)
		if c == int(19):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('chmod +x kalinethunter && bash kalinethunter',shell = True)
			print(colored("[+] Successfully Installed Kali Linux ",color = 'green'))
			print(colored("To Open Kali use - startkali , default username = kali and password = kali, To use kali as root use - startkali -r"))
		if c == int(20):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('apt update && apt upgrade -y && pkg install git -y',shell = True)
			subprocess.call('git clone https://github.com/Ignitetch/AdvPhishing.git',shell = True)
			os.chdir('/data/data/com.termux/files/home/AdvPhishing')
			subprocess.call('chmod +x * && bash Android-Setup.sh',shell = True)
			print(colored("Type This Command - cd AdvPhishing && bash AdvPhishing.sh",color = 'red'))
		if c == int(21):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install wget -y',shell = True)
			subprocess.call('wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh && sh setup.sh && apt install nodejs',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/hax4us/haxRat.git',shell = True)
			os.chdir('/data/data/com.termux/files/home/haxRat/server')
			subprocess.call('npm install',shell = True)
			subprocess.call('mkdir ~/haxrat',shell = True)
			subprocess.call('node index.js',shell = True)
			print(colored("[+] Successfully Installed Haxrat",color = 'green'))
			print(colored('#Note - open your Browser and type localhost:22533 in URL , And the Default Username = admin \nPassword = haxratserver ',color = 'red'))
		if c == int(22):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('wget https://github.com/Hax4us/TermuxBlack/raw/master/install.sh',shell = True)
			print(colored('To Install Any Package Use = apt install pkg_name , ex - apt install lemon',color = 'green'))
			print(colored('To Uninstall Use = rm -f $PREFIX/etc/apt/sources.list.d/termuxblack.list && mv $PREFIX/etc/bash.bashrc.bk $PREFIX/etc/bash.bashrc && rm -f ~/.termux/colors.properties \n ,And restart Your Termux ',color = 'green'))
			subprocess.call('bash install.sh',shell = True)
		if c == int(23):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python python2 -y',shell = True)
			subprocess.call('git clone https://github.com/GUNAWAN18ID/cctv.git && pip2 install requests',shell = True)
			print(colored("[+] Successfully Installed CCTV ",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/cctv')
			subprocess.call('chmod +x * && python2 scanner.py',shell = True)
		if c == int(24):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git -y',shell = True)
			subprocess.call('git clone https://github.com/Bhai4You/Termux-Banner',shell = True)
			os.chdir('/data/data/com.termux/files/home/Termux-Banner')
			subprocess.call('chmod +x *',shell=True)
			os.chdir('/data/data/com.termux/files/home/Termux-Banner')
			subprocess.call('bash requirement.sh && bash t-ban.sh',shell = True)
		if c == int(25):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg update && pkg upgrade && pkg install git cowsay -y',shell = True)
			subprocess.call('git clone https://github.com/Bhaviktutorials/Termux-Keys',shell = True)
			os.chdir('/data/data/com.termux/files/home/Termux-Keys')
			subprocess.call('chmod +x * && bash termux-keys.sh',shell = True)
			print(colored("[+] Successfully Added Extra keys",color = 'green'))
		if c == int(26):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git -y && git clone https://github.com/GhosTmaNHarsh/Ghost-Droid',shell = True)
			print(colored("[+] Successfully Installed Ghost Droid ",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/Ghost-Droid')
			subprocess.call('chmod 777 setup.sh && bash setup.sh && bash ghost-droid',shell = True)
		if c == int(27):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/lovehacker404/Phishing',shell = True)
			print(colored('[+] Successfully Installed BlackMafia',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/Phishing')
			subprocess.call('bash BlackMafia',shell = True)
		if c == int(28):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/Manisso/fsociety',shell = True)
			print(colored('[+] Successfully Installed Fsociety',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/fsociety')
			subprocess.call('bash install.sh',shell = True)
			print(colored("#Note - Please Restart Your Termux and enter These Commands to run Tool -\n cd fsociety && python2 fsociety.py",color = 'red'))
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('logout',shell = True)
			os.chdir('/data/data/com.termux/files/home/fsociety')
			subprocess.call('python2 fsociety.py',shell = True)
		if c == int(29):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python git -y',shell = True)
			subprocess.call('git clone https://github.com/sherlock-project/sherlock',shell = True)
			print(colored("[+] Successfully Installed Sherlock ",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/sherlock')
			subprocess.call('pip3 install -r requiremnts.txt && pip install requests requests_futures torrequest',shell = True)
			yanecl = input("Enter The Username = ")
			yanecl2 = ("python3 sherlock.py "+(yanecl))
			print(colored("#Note - Use This Command = " + "cd sherlock && python3 sherlock.py " +(yanecl),color = 'red'))
		if c == int(30):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install httrack',shell = True)
			print(colored("Successfully Installed Httrack ",color = 'green'))
			print(colored("#Note - use = httrack (website name) , to clone any website"))
		if c == int(31):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python2 -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pip install requests && pip install parse')
			subprocess.call('git clone https://github.com/Dionach/CMSmap.git',shell = True)
			print(colored("Successfully Installed CMS MAP",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/CMSmap')
			subprocess.call('chmod +x * && python2 cmsmap.py -h',shell = True)
		if c == int(32):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/aniketstark/STARK3.0.git',shell = True)
			print(colored("[+] Sucessfully Installed Termux Web Kit",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/STARK3.0')
			subprocess.call('bash install.sh && python2 stark.py',shell = True)
		if c == int(33):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python2 -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git',shell = True)
			print(colored('[+] Successfully Installed D-TECT-1',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/D-TECT-1')
			subprocess.call('chmod +x * && python2 d-tect.py',shell = True)
		if c == int(34):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/NoorQureshi/WPSeku-1',shell = True)
			print(colored('[+] Successfully Installed WPSeku',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/WPSeku-1')
			subprocess.call('chmod +x * && pip install -r requirements.txt',shell = True)
			os.chdir('/data/data/com.termux/files/home/WPSeku-1')
			subprocess.call('python wpseku.py -h',shell = True)
		if c == int(35):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pip install mechaniz',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/Ranginang67/M-dork',shell = True)
			print(colored("[+] Successfully Installed M-DORK",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/M-dork')
			subprocess.call('python2 mdork.py',shell = True)
		if c == int(36):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python python2',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/CiKu370/hasher',shell = True)
			print(colored("[+] Successfully Installed Hash Cracker",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/hasher')
			subprocess.call('python2 hash.py',shell = True)
			print(colored("#Note - If You Installed This First Time So Please Copy And paste this command =  cd hasher && python2 hash.py",color = 'red'))
		if c == int(37):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python python2 -y',shell =True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/sqlmapproject/sqlmap',shell = True)
			print(colored('[+] Successfully Installed sqlmap'))
			os.chdir('/data/data/com.termux/files/home/sqlmap')
			subprocess.call('python2 sqlmap.py',shell = True)
			print(colored('#NOTE = PLEASE SEARCH HOW TO USE SQLMAP ON GOOGLE TO KNOW MORE.',color = 'red'))
		if c == int(38):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('https://github.com/Ranginang67/DarkFly-Tool',shell = True)
			print(colored('[+] Successfully Installed  Dark-Fly ',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/DarkFly-Tool')
			subprocess.call('python2 install.py',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('DarkFly',shell = True)
			print(colored('#Note - To Open DarkFly Anytime Just Type = DarkFly',color = 'red'))
		if c == int(39):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python python2 -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/lightos/credmap',shell = True)
			print(colored('[+] Successfully Installed Credmap',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/credmap')
			subprocess.call('chmod +x *',shell = True)
			print(colored("#Note - Tp Use Credmap Type = cd credmap &&  python2 credmap.py --email MAIL --password PASSWORD\nEXAMPLE:  \npython2 credmap.py --email barneystinson007@gmail.com --password 12345678",color = 'red'))
		if c == int(40):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone hhttps://github.com/fr13nds-group/PhoneSploit',shell = True)
			print(colored(" [+] Successfully Installed PhoneSploit",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/PhoneSploit')
			subprocess.call('pip2 install colorama',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('apt update > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh -q && bash InstallTools.sh',shell = True)
			os.chdir('/data/data/com.termux/files/home/PhoneSploit')
			subprocess.call('python2 main_linux.py',shell = True)
		if c == int(41):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('apt install python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pip2 install requests && pip2 install mechanize',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('rm -rf infect',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/Tech-abm/infect',shell = True)
			print(colored('[+] Successfully Installed Infect',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/infect')
			subprocess.call('python2 infect.xo',shell = True)
		if c == int(42):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install python2 git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/noob-hackers/hacklock',shell = True)
			print(colored('[+] Successfully Installed Hack Lock ',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/hacklock')
			subprocess.call('pip install lolcat',shell = True)
			os.chdir('/data/data/com.termux/files/home/hacklock')
			subprocess.call('bash hacklock.sh',shell = True)
		if c == int(43):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call(''' echo "if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
         command_not_found_handle() {
                 /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
         }
 fi

 PS1='\[\e[31m\]┌─[\[\e[37m\]\T\[\e[31m\]]─────\e[1;98m[@H4Ck3r]\e[0;31m───[\#]\n|\n\e[0;31m└─[\[\e[31m\]\e[0;35m\W\[\e[31m\]]────►\e[1;93m'" > /data/data/com.termux/files/usr/etc/bash.bashrc && exit''',shell = True)
			print(colored('''#Note To Uninstall Parrot Os Type This Command = echo "if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
         command_not_found_handle() {
                 /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
         }
 fi
 PS1='\$ '" > /data/data/com.termux/files/usr/etc/bash.bashrc && exit ''',color = 'red'))
		if c == int(44):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone git://github.com/htr-tech/nexphisher.git',shell = True)
			print(colored('[+] Successfully Installed Nexphish',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/nexphisher')
			subprocess.call('bash tmux_setup',shell = True)
			os.chdir('/data/data/com.termux/files/home/nexphisher')
			subprocess.call('bash nexphisher',shell = True)
		if c == int(45):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/termuxprofessor/Telegram-Scraper-Adder',shell = True)
			print(colored('Successfully Installed Telegram Member Adder Script',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/Telegram-Scraper-Adder')
			subprocess.call('chmod +x setup.py',shell = True)
			os.chdir('/data/data/com.termux/files/home/Telegram-Scraper-Adder')
			subprocess.call('python setup.py',shell = True)
			print(colored(''' #NOTE - \nenter api I'd
Enter hash I'd
Enter mob. No.

cd Telegram-Scraper-Adder && python scraper.py

Now enter verification code came to your no. 

Choose group 

Now subscribe termux professor yt channel

python adder.py

Choose group again u want to add member

Now select the way you want to add through I'd or username 

Boom! You are done'''))
		if c == int(46):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git python -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/Gameye98/Lazymux',shell = True)
			print(colored("[+] Successfully Installed Lazymux",color = 'green'))
			os.chdir('/data/data/com.termux/files/home/Lazymux')
			subprocess.call('python lazymux.py',shell = True)
		if c == int(47):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git php -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/s0md3v/ReconDog',shell = True)
			print(colored('[+] Successfully Installed ReconDog',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/ReconDog')
			subprocess.call('pip install -r requirements.txt',shell = True)
			os.chdir('/data/data/com.termux/files/home/ReconDog')
			subprocess.call('python dog',shell = True)
		if c == int(48):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install x11-repo -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('apt install wireshark-gtk xterm tigervnc tigervnc-viewer -y',shell = True)
			print(colored("[+] Successfuly Installed Wireshark",color = 'green'))
			print(colored("#NOTE - TO GET PROPER GUIDE ON HOW TO USE THIS TOOL VISIT HERE = https://www.learntermux.tech/2020/10/Install-WireShark-IN-Termux.html?m=1",color = 'red'))
		if c == int(49):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/ExpertAnonymous/T-LOAD',shell = True)
			print(colored('[+] Successfully Installed T-LOAD',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/T-LOAD')
			print(colored('#Note -To reverse This Use = cd T-LOAD && bash rvt.sh',color = 'red'))
			subprocess.call('bash t-load.sh',shell = True)
		if c == int(50):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('https://github.com/Lexiie/Termux-Apktool')
			print(colored("[+] Successfully Installed Termux-Apktool",color ='green'))
			os.chdir('/data/data/com.termux/files/home/Termux-Apktool')
			subprocess.call('dpkg -i apktool_2.3.4_all.deb',shell =True)
			os.chdir('/data/data/com.termux/files/home/Termux-Apktool')
			subprocess.call('apktool',shell = True)
			print(colored("#Note -Search How To Use Termux ApkTool On Google To know More...",color = 'red'))
		if c == int(51):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('apt install php wget git -y',shell = True)
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('git clone https://github.com/kinghacker0/WishFish.git',shell = True)
			print(colored('[+] Successfully Installed MadCam',color = 'green'))
			os.chdir('/data/data/com.termux/files/home/WishFish')
			subprocess.call('bash copy.sh',shell = True)
			os.chdir('/data/data/com.termux/files/home/WishFish')
			print(colored("#Note - Please Turn On Your Hotspot",color = 'red'))
			subprocess.call('bash wishfish.sh',shell = True)
		if c == int(52):
			os.chdir('/data/data/com.termux/files/home')
			subprocess.call('pkg install nano',shell = True)
			print(colored('[+] Successfully Installed Nano',color = 'green'))
			print(colored('#Note -  To Open Existing File = nano (file name) or making a new file , simply type = nano',color = 'red'))
		if c == int(53):
			os.system('clear')
			print(colored("\t I Am Glad That You Gave Your Precious Time To know About Me!",color = 'red'))
			print("\n\n\n")
			print(colored("My Name Is = LegendPikachu \n And I love Making tools \n \n I Have Made Many Paid and Free Tools \n\n What is My Age? \n Ans. 14 Years \n\nWhy I Made This Tool ? \n To Make It Easier For accessing Any Tool \n I Will Update This Tool And Make It Even More Better Well Untill Than \nEnjoy This v1 Of This Tool !!",color = 'cyan'))
			print(colored("\n\n And Also Special Thanks To The Creator of These Tools!! \n\n",color = "magenta"))
			print(colored('You Can Contact Me Here = https://t.me/LegendPikachu_YT',color = 'green'))
			print(colored('\nTo Know More About Me = https://t.me/AboutDarkiecrif',color = 'green'))
			print(colored("\n\nYou Can Also Recommend Me Which Tool Should I Make Next \n\n \tOnce Again I Do Not Promote Any Illegal Use Of This Tool",color = 'red'))
			msg=(colored('''\n\n \tThank You Very Much ''',color = 'blue'))
			for i in msg:
			     sys.stdout.write(i)
			     sys.stdout.flush()
			     time.sleep(0.02)
			msg2=(colored('''\n\t I Will Be Back With More Amazing Tools Bye Bye!\n''',color = 'blue'))
			for i in msg2:
			     sys.stdout.write(i)
			     sys.stdout.flush()
			     time.sleep(0.02)
		if c == int(54):
			print(colored('Exiting The Tool...',color = 'green'))
			exit
	else:
		print(colored("\n\nTHE ACCESS KEY THAT YOU HAVE ENTERED IS WRONG",color = 'red'))
		exit
elif a == "n":
	print(colored("\n\nEXITING THE TOOL",color = 'yellow'))
	exit
else:
	print("\n\nTHIS IS NOT A VALID OPTION, EXITING THE POKEBALL")
	exit
