# Timing function execution 
# Write a decorator that mesures the time a function takes to execute

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def long_running_function():
    time.sleep(2)  # Simulating a long-running task
    return "Task completed" 



# Applying the decorator to the function
timed_long_running_function = timing_decorator(long_running_function)
# Calling the decorated function
print(timed_long_running_function())



# Output:
# Execution time: 2.002345561981201 seconds
# Task completed
