import time

def runtime_wrapper(func):
    start_time = time.time()
    func()
    end_time = time.time()
    runtime = end_time - start_time * 1000
    print(f"Runtime: {runtime:.4f} ms")