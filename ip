import sys 
import os 
import socket


def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ip_addr = socket_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', inter[:15]))[20:24])
	return ip_addr
