import logging
import threading
import time
import pid
import random

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


class RepeatedTimer(object):
    def __init__(self, interval, function, *args):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def updateArgs(self, *args):
        self.args = args

    def stop(self):
        self._timer.cancel()
        self.is_running = False

		
# name, P, I, D, Derivator, Integrator, Integrator_max, Integrator_min, set_point,set_point_max, set_point_min 
roll = pid.PID_RP("roll", 2.0, 1.0, 0.0, 0, 0, 20000, -20000, 0.0, 1000 -1000)
#pitch = pid.PID_RP("pitch", 2.0, 1.0, 0.0, 0, 0, 20000, -20000, 0.0, 1000 -1000)

# test current state for pids
projloc = [0.0,0.0,0.0]
projvel = [1.0,1.0,1.0]

projtarget = [1.0,1.0,0.0]


# 8 milliseconds
ts = 0.1
	

if __name__ == '__main__':

    # create objects for the repeating threads for pids
    rollThread = RepeatedTimer(ts, pid.PID_RP.update, roll, projloc[0]) 
    #pitchThread = RepeatedTimer(ts, pid.PID_RP.update, pitch, projloc[1]) 

    roll.set_point_to(projtarget[0])
    #pitch.set_point_to(projtarget[1])

    while(1):
        
        # add to the location of the quad (simulate movement)
        for i in range(0,40):

            # roll pid
            projloc[0] = projloc[0] + 0.025
            rollThread.updateArgs(roll, projloc[0])

            # pitch pid
            #projloc[1] = projloc[1] + 0.025
            #pitchThread.updateArgs(pitch, projloc[1])

            time.sleep(0.1)



