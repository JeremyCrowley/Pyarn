import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    logging.debug('Starting')
    state[3] = 0
    logging.debug('Exiting')




state = [0, 0, 0, 1]



def main():

	while(1):

		w = threading.Thread(name='worker', target=worker)
		
		if(state[3] == 1):
			w.start()

		time.sleep(3)

		state[3] = 1



if __name__ == '__main__':
	main()


