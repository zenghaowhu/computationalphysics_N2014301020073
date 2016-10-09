import pylab as pl
class uranium_decay_A_and_B:
    N_A = int(input("Input Initial number of nuclei_A :"))
    N_B = int(input("Input Initial number of nuclei_B :"))
    t_c = eval(input("Input time constant :"))
    t_d = eval(input("input time of duration :"))
    t_s = eval(input("Input time step :"))
    def __init__(self, number_of_nuclei_A = N_A, number_of_nuclei_B =N_B, time_constant =t_c, time_of_duration =t_d, time_step =t_s):
        # unit of time is second
        self.n_uranium_A = [number_of_nuclei_A]
        self.n_uranium_B = [number_of_nuclei_B]
        self.init_A = number_of_nuclei_A
        self.init_B = number_of_nuclei_B
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei_A ->", number_of_nuclei_A)
        print("Initial number of nuclei_B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_uranium_A[i] + (self.n_uranium_B[i] - self.n_uranium_A[i]) * self.dt
            tmp_B = self.n_uranium_B[i] + (self.n_uranium_A[i] - self.n_uranium_B[i]) * self.dt
            self.n_uranium_A.append(tmp_A)
            self.n_uranium_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_uranium_A, 'b', label = "$N_A$")
        pl.plot(self.t, self.n_uranium_B, 'r', label = "$N_B$")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0, self.time)
        pl.legend()
        pl.show()
a = uranium_decay_A_and_B()
a.calculate()
a.show_results()
