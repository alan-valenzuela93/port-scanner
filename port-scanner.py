import socket
import argparse

def scan(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, port))
		s.settimeout(0.2) #Increase scanning speed
	except:
		return False
	else:
		return True

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', help='Enter your target adress')
	parser = parser.parse_args()
	ports = [21, 22, 25, 53, 66, 80, 88, 110, 443, 8080, 9050] #This are some of the most interesting ports to scan
	result = dict() #I save the result as a dictionary, with the port as the key and the status as it's value.

	for p in ports:
		if(scan(parser.target, p)):
			result.setdefault(p, 'OPEN')
		else:
			result.setdefault(p, 'CLOSE')

	print('')
	print('PORT | STATUS')
	print('')
	
	for key, value in result.items():
		print(key, '   ', value)

if __name__ == '__main__':
	print('Scanning started...')
	print('')
	main()
