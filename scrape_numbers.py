import phonenumbers
import requests
import threading
import time
import string
import random
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sites = [
	"https://receive-sms-online.info/",
	"https://receive-smss.com/",
	"https://sms24.me/numbers",
	"https://www.receivesms.co/active-numbers/",
	"https://receive-sms.cc/",
	"https://sms-receive.net/",
	"https://getfreesmsnumber.com/free-receive-sms-from-au",
	"https://getfreesmsnumber.com/free-receive-sms-from-be",
	"https://getfreesmsnumber.com/free-receive-sms-from-ca",
	"https://getfreesmsnumber.com/free-receive-sms-from-fr",
	"https://getfreesmsnumber.com/free-receive-sms-from-pl",
	"https://getfreesmsnumber.com/free-receive-sms-from-se",
	"https://getfreesmsnumber.com/free-receive-sms-from-uk",
	"https://getfreesmsnumber.com/free-receive-sms-from-us",
	"https://getfreesmsnumber.com/free-receive-sms-from-vn",
	"https://sms-online.co/receive-free-sms",
	"https://freephonenum.com/us",
	"https://freephonenum.com/ca",
	"https://smstools.online/receive-free-sms/canada/",
	"https://smstools.online/receive-free-sms/australia/",
	"https://smstools.online/receive-free-sms/germany/",
	"https://smstools.online/receive-free-sms/france/",
	"https://smstools.online/receive-free-sms/belgium/",
	"https://receive-sms-free.net/",
	"https://www.receivesmsonline.net/",
	"https://www.freeonlinephone.org/",
	"http://sms.sellaite.com/",
	"https://5sim.net/v1/guest/free",
	"http://7sim.net/",
	"https://receive-sms.com/",
	"https://receiveasms.com/",
	"https://receivesms.cc/country",
	"http://receivefreesms.com/",
	"https://pingme.tel/receive-sms-online/",
	"https://sms-receive.com/",
	"http://www.s-sms.com/",
	"https://sms-online.pl/",
	"https://freesmscode.com/",
	"https://hs3x.com/",
	"https://en.yinsiduanxin.com/",
	"https://online-sms.org/"
]
extracted_numbers = []
countries = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR","AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE","BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO","BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD","CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI","HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG","SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF","PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD","GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN","HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT","JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG","LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK","MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT","MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA","NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP","NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN","PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN","LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC","SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES","LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ","TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV","UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN","VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
threads_running = []

def country_thread(text, country):
	global threads_running
	global extracted_numbers
	thread_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))
	threads_running.append(thread_id)
	phonenumbermatcher = phonenumbers.PhoneNumberMatcher(text, country)
	for match in phonenumbermatcher:
		extracted_numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
	threads_running.remove(thread_id)
	
def site_thread(site):
	global threads_running
	global countries
	thread_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))
	threads_running.append(thread_id)
	print("Processing " + site)
	try:
		site_html = requests.get(site, verify=False, timeout=5, allow_redirects=True)
		if not site_html.text or site_html.text == "":
			threads_running.remove(thread_id)
			return
		print("Processed " + site)
	except Exception as e:
		threads_running.remove(thread_id)
		return
	text = site_html.text
	for country in countries:
		t = threading.Thread(target=country_thread, args=(text, country,))
		t.start()
	threads_running.remove(thread_id)
	
def main():
	global threads_running
	global extracted_numbers
	for site in sites:
		t = threading.Thread(target=site_thread, args=(site,))
		t.start()
				
	while True:
		print("Number of threads running: " + str(len(threads_running)))
		if not threads_running:
			time.sleep(0.5) # Sleep 500 milliseconds to make sure all the threads have really finished.
			if threads_running:
				# Nope, the threads didn't really finish yet.
				continue
			else:
				# All threads finished, continue main function.
				break
		time.sleep(1)
			
	extracted_numbers = list(set(extracted_numbers))
	
	for number in extracted_numbers:
		# Do whatever you want here with the extracted numbers...
		print(number)
			
	print("All done!")
	
if __name__ == "__main__":
	main()