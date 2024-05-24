from modules.eval_multi_env import run_multi_eval
from modules.migration_runner import run_migration
from modules.rg_runner import run_rg
import threading
import time

'''
It's just fun :)
'''
def show_banner():
    print()
    print("        ██       ")
    print("          ██     ")
    print("      ████████   ")
    print("         ███████ ")
    print("██ LAUNCHDARKLY █")
    print("         ███████ ")
    print("      ████████   ")
    print("          ██     ")
    print("        ██       ")
    print()


'''
Create threads to run all population tools in parallel
'''
multi_eval = threading.Thread(target=run_multi_eval)
migration = threading.Thread(target=run_migration)
rg = threading.Thread(target=run_rg)


'''
EXECUTE
'''
if __name__ == '__main__':
    show_banner()
    multi_eval.start()
    migration.start()
    rg.start()
    time.sleep(5)
    multi_eval.join()
    migration.join()
    rg.join()
    print("*** All threads have finished. Shutting down. ***")
