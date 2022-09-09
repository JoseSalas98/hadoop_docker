from time import sleep, perf_counter


def task():
    """function executes and sleeps for one second. Then it executes the second time and also sleeps for 
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
