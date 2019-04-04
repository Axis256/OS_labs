class Processor:
    def __init__(self, proc_list):
        self.remote_proc_list = proc_list
        self.__cur_time = 0
        self.__res_time = 0
        self.finished_procs = 0
        self.running_procs = 0
        self.proc_list = []
        self.done_processing = False

    def inc_idle_time(self, time_inc):
        self.__cur_time += time_inc

    def process(self, proc, time_inc):
        self.inc_idle_time(time_inc)
        self.__res_time += time_inc * self.running_procs
        proc -= time_inc

    def add_next_process(self):
        i = 0
        while i < len(self.remote_proc_list):
            if self.__cur_time >= self.remote_proc_list[i][0]:
                self.proc_list.append(self.remote_proc_list[i][1])
                self.running_procs += 1
                i += 1
                yield
            else:
                yield
        self.done_processing = True

    def termination_check(self, proc_time):
        if proc_time == 0:
            self.running_procs -= 1
            self.finished_procs += 1
