from ldclient import Result
import json
import random
import time
from dotenv import load_dotenv


def write_new():
    def randomizer(error_rate):
        new_rate = error_rate['new']
        value = random.randint(1, 1000)
        # Intentional pause to simulate write latency
        time.sleep(.2)
        if value >= new_rate:
            return Result.success("Write: Success")
        else:
            return Result.fail("Write: Fail")
    return randomizer

def write_old():
    def randomizer(error_rate):
        old_rate = error_rate['old']
        value = random.randint(1, 1000)
        # Intentional pause to simulate write latency
        time.sleep(.35)
        if value >= old_rate:
            return Result.success("Write: Success")
        else:
            return Result.fail("Write: Fail")
    return randomizer

def read_new():
    def randomizer(error_rate):
        new_rate = error_rate['new']
        value = random.randint(1, 1000)
        # Intentional pause to simulate read latency
        time.sleep(.2)
        if value >= new_rate:
            # Add an additional check on succesful read to determine whether this will be consistent with the other read
            consistency_value = random.randint(1, 1000)
            if consistency_value <= 998:
                return Result.success("Read: Consistent")
            else: 
                return Result.success("Read: Inconsistent")
        else:
            return Result.fail("Read: Fail")
    return randomizer

def read_old():
    def randomizer(error_rate):
        old_rate = error_rate['old']
        value = random.randint(1, 1000)
        # Intentional pause to simulate read latency
        time.sleep(.4)
        if value >= old_rate:
            # Add an additional check on succesful read to determine whether this will be consistent with the other read
            consistency_value = random.randint(1, 1000)
            if consistency_value <= 998:
                return Result.success("Read: Consistent")
            else: 
                return Result.success("Read: Inconsistent")
        else:
            return Result.fail("Read: Fail")
    return randomizer

def consistency_check():
    def check_consistency(a, b):
        if a == b:
            return True
        else:
            return False
    return check_consistency
