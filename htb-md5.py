import hashlib
from bs4 import BeautifulSoup
import requests


def md(port):
	url = 'http://docker.hackthebox.eu:{}/'.format(port)
	r = requests.session()
	req = r.get(url)

	scrape = BeautifulSoup(req.text, 'lxml')
	for target in scrape.find_all("h3"):
		print("[+] String: ", target.text)

		key = hashlib.md5(str.encode(target.text)).hexdigest()
		print("[+] Hash: ", key)

		payload = {'hash': key}
		post_key = r.post(url, payload)

		scrape2 = BeautifulSoup(post_key.text, 'lxml')
		for flag in scrape2.find_all("p"):
			print("[+] Flag: ", flag.text)

# Port number of running instance
dst = input("Enter destination port: ")
md(dst)
