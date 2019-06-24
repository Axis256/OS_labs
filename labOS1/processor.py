from copy import copy


class Processor:
    def __init__(self, proc_list):
        self.remote_proc_list = copy(proc_list)
        self.__cur_time = 0
        self.__res_time = 0
        self.finished_procs = 0
        self.running_procs = 0
        self.proc_list = []
        self.done_processing = False

    def inc_idle_time(self, time_inc):
        self.__cur_time += time_inc

    def process(self, proc_ind, time_inc):
        self.inc_idle_time(time_inc)
        self.__res_time += time_inc * self.running_procs
        self.proc_list[proc_ind] -= time_inc

    def add_next_process(self):
        if len(self.remote_proc_list) > 0 and self.__cur_time >= self.remote_proc_list[0][0]:
            self.proc_list.append(self.remote_proc_list[0][1])
            self.remote_proc_list.popleft()
            self.running_procs += 1
            self.add_next_process()
            return len(self.proc_list) - 1
        else:
            return None

    def termination_check(self, proc_ind):
        if self.proc_list[proc_ind] == 0:
            self.running_procs -= 1
            self.finished_procs += 1
            return True
        else:
            return False

    def get_avg_res_time(self):
        return self.__res_time / self.finished_procs
