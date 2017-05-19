import logging
import threading
import time
from multiprocessing.pool import ThreadPool

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

xdes = [0.0, 0.0, False];
x = 0.0
y = 0.0
z = 0.0
px = 0.0
py = 0.0
pz = 0.0
pxdot = 0.0
pydot = 0.0
pzdot = 0.0

def mpc(x,y,z,px,py,pz,pxdot,pydot,pzdot):
    logging.debug('Starting mpc')
    time.sleep(0.038)
    logging.debug('Exiting mpc')
    return True


pool = ThreadPool(processes=1)
TrajectoryPlanner = pool.apply_async(mpc, (x,y,z,px,py,pz,pxdot,pydot,pzdot)) # tuple of args for foo
threadFin = False
while(1):

	start = time.time()
	if(threadFin == True):
		TrajectoryPlanner = pool.apply_async(mpc, (x,y,z,px,py,pz,pxdot,pydot,pzdot)) # tuple of args for foo
		threadFin = False

	time.sleep(0.008)


	if(TrajectoryPlanner.ready()):
		return_val = TrajectoryPlanner.get() # get the return value from your function.
		threadFin = True

	logging.debug(threadFin)

	print(time.time() - start)


# current state

"""
def main():
	
	mpcthread = threading.Thread(name='mpcrun', target=mpc, args=xdes[3])


	while 1:

		# restart thread if 
		if(not mpcthread.isAlive()):

			mpcthread = threading.Thread(name='mpcrun', target=mpc, args=(self,xdes))
			mpcthread.start()

if __name__ == '__main__':
	main()
"""