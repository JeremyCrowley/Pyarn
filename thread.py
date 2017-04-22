import logging
import threading
import time
import pid

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    logging.debug('Starting')
    state[3] = 0
    logging.debug('Exiting')




state = [0, 0, 0, 1]



def main():
	i = 0
	while(1):

		w = threading.Thread(name='worker', target=worker)
		
		if(state[3] == 1):
			w.start()

		

		if(i == 4):
			state[3] = 1
			i = 0

		i = i + 1

		time.sleep(2)
		print(state)
		time.sleep(1)


if __name__ == '__main__':
	main()


