from src.shared.utils.dates import UtilDates
from src.shared.utils.colors import bcolors

def log_task(func):
    def wrapper(self, *args, **kwargs):
        dates = UtilDates()
        datestart = dates.time_now()
        print(f'\n{bcolors.BLUE}[{func.__name__.upper()}]{bcolors.ENDC} - Start at {datestart}')
        
        result = func(self, *args, **kwargs)
        
        print(f'\n{bcolors.BLUE}[{func.__name__.upper()}]{bcolors.ENDC} - Finished at {dates.time_now()}')
        print(f'\n{bcolors.BLUE}[{func.__name__.upper()}]{bcolors.ENDC} - Execution time {dates.result_execution_time(datestart)}s')
        
        return result
    return wrapper