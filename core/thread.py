from time import sleep, perf_counter
from threading import Thread


def task():
    """This function executes and sleeps for one second. Then it executes the second time and also sleeps for 
    another second
    """
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

#   the program takes about one seconds to complete. If you call the task() function 5 times,
#   it would take about 5 seconds to complet...

# 1
task()
# 2
task()
# 3
task()
# 4
task()
# 5
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

#   use python threading to develop a multi-threaded program

start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

#   the output showns, the program took one second instead of
#   two to complete
