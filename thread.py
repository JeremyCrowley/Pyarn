import logging
import threading
import time
import pid

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

def worker():
    logging.debug('Starting')
    state[3] = 0
    logging.debug('Exiting')


# name, P, I, D, Derivator, Integrator, Integrator_max, Integrator_min, set_point,set_point_max, set_point_min 
testpid = pid.PID_RP("test", 2.0, 0.0, 1.0, 0, 0, 20000, -20000, 0.0, 1000 -1000)

# current state
x = 0.01

def main():
	i = 0

	#w = threading.Thread(name='worker', target=worker)
	up = threading.Thread(name='pidupdate', target=pid.PID_RP.update, args=(testpid, x))
	
	while 1:

		# restart thread if 
		if(not up.isAlive()):
			up = threading.Thread(name='pidupdate', target=pid.PID_RP.update, args=(testpid, x))
			up.start()

if __name__ == '__main__':
	main()


