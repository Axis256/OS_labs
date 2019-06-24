from random import randint
from processor import Processor
from collections import deque


def gen_processes():
    p_count = randint(30, 50)
    proc_list = deque(maxlen=p_count)
    proc_list.append((0, randint(2, 10)))
    for i in range(1, p_count):
        proc_list.append((proc_list[-1][0] + randint(2, 10), randint(4, 8)))
    return proc_list


def round_robin(proc_list):
    cpu = Processor(proc_list)
    cpu.add_next_process()
    while not cpu.done_processing:
        if cpu.running_procs == 0:
            cpu.inc_idle_time(1)
            cpu.add_next_process()
        else:
            for i in range (len(cpu.proc_list)):
                if cpu.proc_list[i] > 0:
                    cpu.process(i, min(cpu.proc_list[i], 2))
                    cpu.termination_check(i)
                    cpu.add_next_process()
        if cpu.finished_procs == len(proc_list):
            cpu.done_processing = True
    return cpu.get_avg_res_time()


def SRT(proc_list):

    def find_min_time(proc_list):
        min_time = 11
        index = -1
        for i in range(len(proc_list)):
            if proc_list[i] < min_time and proc_list[i] != 0:
                min_time = proc_list[i]
                index = i
        if min_time == 0 or index == -1:
            return None
        else:
            return index

    cpu = Processor(proc_list)
    cpu.add_next_process()
    cur_proc_index = 0
    while not cpu.done_processing:
        if cur_proc_index is None:
            cpu.inc_idle_time(1)
            ind = cpu.add_next_process()
            if ind is not None:
                cur_proc_index = ind
        else:
            cpu.process(cur_proc_index, 1)
            new_proc_index = cpu.add_next_process()
            if new_proc_index is not None and cpu.proc_list[new_proc_index] < cpu.proc_list[cur_proc_index]:
                cur_proc_index = new_proc_index
            elif cpu.termination_check(cur_proc_index):
                cur_proc_index = find_min_time(cpu.proc_list)
        if cpu.finished_procs == len(proc_list):
            cpu.done_processing = True
    return cpu.get_avg_res_time()

procs = gen_processes()
print('Round robin (4) average residence time:', round_robin(procs))
print('SRT average residence time:', SRT(procs))
