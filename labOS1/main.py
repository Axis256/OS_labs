from random import randint
from processor import Processor


def gen_processes():
    p_count = randint(30, 50)
    proc_list = [(0, randint(2, 10))]
    for i in range(1, p_count):
        proc_list.append((proc_list[i - 1][0] + randint(2, 10), randint(4, 8)))
    return proc_list


def round_robin(proc_list):
    cpu = Processor(proc_list)
    next(cpu.add_next_process())
    # cpu.add_next_process()
    while not cpu.done_processing:
        if cpu.running_procs == 0:
            cpu.inc_idle_time(1)
            next(cpu.add_next_process())
        else:
            for proc_time in cpu.proc_list:
                if proc_time > 0:
                    cpu.process(proc_time, min(proc_time, 2))
                    cpu.termination_check(proc_time)
                    next(cpu.add_next_process())
                    print(cpu.running_procs, cpu.finished_procs)
                    print(cpu.proc_list)


# def round_robin(proc_list):
#     local_list = [copy(proc_list[0])]
#     next_ind = 1
#     finished_procs = 0
#     running_procs = 1
#     cur_time = 0
#     res_time = 0
#     while finished_procs < len(proc_list):
#         if running_procs == 0:
#             cur_time += 1
#             if next_ind < len(proc_list) and proc_list[next_ind][0] <= cur_time:
#                 local_list.append(proc_list[next_ind])
#                 running_procs += 1
#                 next_ind += 1
#         else:
#             for proc in local_list:
#                 if proc[1] > 0:
#                     print(local_list)
#                     print(running_procs, cur_time, res_time)
#                     res_time += min(2, proc[1]) * running_procs
#                     cur_time += min(2, proc[1])
#                     proc[1] -= min(2, proc[1])
#                     if proc[1] == 0:
#                         finished_procs += 1
#                         running_procs -= 1
#                     if next_ind < len(proc_list) and proc_list[next_ind][0] <= cur_time:
#                         local_list.append(proc_list[next_ind])
#                         running_procs += 1
#                         next_ind += 1
#     print(res_time, finished_procs)
#     return res_time / finished_procs


# def SRT(proc_list):
#
#     def find_min_time(proc_list):
#         min_time = 11
#         index = -1
#         for i in range(len(proc_list)):
#             if proc_list[i][1] < min_time:
#                 min_time = proc_list[i][1]
#                 index = i
#         if min_time == 0:
#             return -1
#         else:
#             return index
#
#     local_list = proc_list[0]
#     next_ind = 1
#     finished_procs = 0
#     running_procs = len(local_list)
#     time = 0
#     while finished_procs < len(proc_list):
#         if find_min_time(local_list) != -1:
#             proc = proc_list[find_min_time(local_list)]
#         time += 1
#         if proc_list[next_ind][0] >= time:
#             local_list.append(proc_list[next_ind])
#             if next_ind + 1 < len(proc_list):
#                 next_ind += 1

print(round_robin(gen_processes()))
