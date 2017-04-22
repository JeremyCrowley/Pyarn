import time


class PID_RP:
    """

    Standard digital PID - backwards euler implementation

    """

    def __init__(self, name="N/A", P=1.0, I=0.0, D=10.0, Derivator=0, Integrator=0, Integrator_max=20000,
                 Integrator_min=-20000, set_point=0.0, power=1.0 ,set_point_max = 1000,set_point_min = -1000):
        self._zmq = zmq_connection
        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.name = name
        self.set_point_max = set_point_max
        self.set_point_min = set_point_min
        self.set_point=set_point

        #e,e1,e2 are e[k], e[k-1], e[k-2] from the difference equation. 
        self.e = 0
        self.e1 = 0
        self.e2 = 0

        #u,u1,u2 are u[k], u[k-1], u[k-2] from the difference equation. 
        self.u = 0
        self.u1 = 0
        self.u2 = 0

        #Ts is not currently known, so it is set to .01s here. N is for the low pass filter on the derivative term
        self.Ts = 0.01
        self.N = 5

        self.prev_t = 0

    def reset_dt(self):
        self.prev_t = time.time()

    def update(self, currentState):
    	"""
		Update control input
    	"""
       
        self.e2 = self.e1
        self.e1 = self.e
        self.e = self.set_point - currentState
        self.u2 = self.u1
        self.u1 = self.u
      
        b0 = self.Kp*(1 + (self.N*self.Ts)) + self.Ki*self.Ts*(1 + (self.N*self.Ts)) + self.Kd*self.N
        b1 = -1*(self.Kp*(2 + (self.N*self.Ts)) + self.Ki*self.Ts + 2*self.Kd*self.N)
        b2 = self.Kp + self.Kd*self.N
        a0 = 1 + self.N*self.Ts
        a1 = -1*(2 + self.N*self.Ts)
        a2 = 1

        # Final control input returned by PID's.
        self.u = -1*((a1/a0)*(self.u1) + (a2/a0)*(self.u2)) + ((b0/a0)*self.e + (b1/a0)*self.e1 + (b2/a0)*self.e2)

        return self.u

    def set_point_to(self,set_point):
        """
        Initilize the setpoint of PID
        """
        if set_point > self.set_point_max:
            self.set_point = self.set_point_max
            return
        elif set_point < self.set_point_min:
            self.set_point = self.set_point_min
            return
        self.set_point = set_point
















