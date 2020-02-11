#!/usr/bin/python3

# l293d documentation from:  https://github.com/jmsv/l293d

#import l293d.driver as l293d
import l293d

def main():
	''' main function'''

	# Motor 1 uses Pin 22, Pin 18, Pin 16
	motor = l293d.DC(22,18,16)
	motor.clockwise(duration=3, speed=25)

	# Run the motors so visible
	#for i in range(0,1500):
	#	motor.clockwise()

	l293d.cleanup()


if __name__ == '__main__':
	main()
