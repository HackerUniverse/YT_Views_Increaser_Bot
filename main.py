import re
import requests
from os import _exit
from time import sleep
from random import choice,uniform
from argparse import ArgumentParser
from threading import Thread
from traceback import print_exc
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType

parser=ArgumentParser()
parser.add_argument('-t','--threads',type=int,help='set number of the threads',default=15)
parser.add_argument('-u','--url',help='set url of the video',default='',required=True)
parser.add_argument('-d','--duration',help='set the duration of the video in seconds',default=5*60)
parser.add_argument('-p','--proxies',help='set the path of the proxies list')
parser.add_argument('-us','--user-agent',help='set the user agent for the driver')
parser.add_argument('-uss','--user-agents',help='set the path of the list of the user agents for the driver')
parser.add_argument('-dr','--driver',help='set the driver for the bot',choices=['chrome','firefox'],default='chrome')
args=parser.parse_args()

def bot(url):
	try:
		while True:
			proxy.http_proxy=choice(proxies)
			proxy.ssl_proxy=proxy.http_proxy
			print(proxy.http_proxy)
			if args.driver=='chrome':
				chrome_options.add_argument('user-agent="{}"'.format(args.user_agent or (args.user_agents and choice(user_agents)) or agent.random))
				capabilities=webdriver.DesiredCapabilities.CHROME
				proxy.add_to_capabilities(capabilities)
				driver=webdriver.Chrome(options=chrome_options,desired_capabilities=capabilities)
			else:
				firefox_profile.set_preference('general.useragent.override',args.user_agent or (args.user_agents and choice(user_agents)) or agent.random)
				firefox_profile.set_preference('network.proxy.type',1)
				firefox_profile.set_preference('network.proxy.http',proxy.http_proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.http_port',proxy.http_proxy.split(':')[1])
				firefox_profile.set_preference('network.proxy.ssl',proxy.ssl_proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.ssl_port',proxy.ssl_proxy.split(':')[1])
				firefox_profile.update_preferences() 
				driver=webdriver.Firefox(firefox_profile=firefox_profile)
			driver.get(args.url)
			sleep(float(args.duration))
			driver.close()
	except KeyboardInterrupt:_exit(0)
	except Exception:
		print_exc()
		_exit(1)

try:
	if args.proxies:
		proxies=open(args.proxies,'r').read().split('\n')
	else:
		proxies=re.findall(re.compile('<td>([\d.]+)</td>'),str(requests.get('https://free-proxy-list.net/').content))
		proxies=['%s:%s'%x for x in list(zip(proxies[0::2],proxies[1::2]))]
	print('%d proxies successfully loaded!'%len(proxies))
	proxy=Proxy()
	proxy.proxy_type=ProxyType.MANUAL
	if args.user_agents:
		user_agents=open(args.user_agents,'r').read().split('\n')
	else:
		agent=UserAgent()
	if args.driver=='chrome':
		chrome_options=webdriver.ChromeOptions()
		chrome_options.add_argument('--mute-audio')
	else:
		firefox_profile=webdriver.FirefoxProfile()
		firefox_profile.set_preference('media.volum_scale','0.0')
	for i in range(args.threads):
		t=Thread(target=bot,args=(args.url,))
		t.deamon=True
		t.start()
		sleep(uniform(2.0,4.0))
except KeyboardInterrupt:_exit(0)
except Exception:
	print_exc()
	_exit(1)