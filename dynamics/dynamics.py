'''
Base class for dynamics models.
'''
class Dynamics(object):
    def __init__(self, x_dim, u_dim, r_dim):
        print("Init Dynamics")
        super(Dynamics, self).__init__()
        self.x_dim = x_dim
        self.u_dim = u_dim
        self.r_dim = r_dim


