import psutil
import shutil
import socket
import requests


def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free 

def check_cpu_usage():
	usage  = psutil.cpu_percent(1)
	return usage

def check_connectivity():
	request = requests.get("http://www.google.com")
	return request.status_code == 200

def check_localhost():
	localhost = socket.gethostbyname('localhost')
	return localhost 

def run_Check():
	print("Disk space free: %{:.2f} \nCPU usage: %{}".format(check_disk_usage("/"),check_cpu_usage()))
	if check_connectivity():
		print("Connection: OK")
	else:
		print("Connection: Not OK")
	print("Local Host is: {}".format(check_localhost()))