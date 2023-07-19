import psutil


def get_cpu_times():
    cpu_times = psutil.cpu_times()
    cpu_times_info = {
        "user": cpu_times.user,
        "system": cpu_times.system,
        # "idle": cpu_times.idle,
        # "interrupt": cpu_times.interrupt,
        # "dpc": cpu_times.dpc,
    }

    return cpu_times_info


def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count


def get_loadavg():
    loadavg = psutil.getloadavg()
    return loadavg

def get_virtual_memory():  
    virtual_memory = psutil.virtual_memory()
    return virtual_memory


def get_swap_memory():
    swap_memory = psutil.swap_memory()
    return swap_memory
