#!/usr/bin/env python3
from datetime import datetime
import time

def isoformat8601(t):
    s = t.astimezone().isoformat()
    return f"{s[:-6]}Z{s[-6:]}"

with open("outtest.txt", "a") as f:
    f.write(f"Start at {isoformat8601(datetime.now())}\n")
    time.sleep(3)
    f.write(f"End at {isoformat8601(datetime.now())}\n\n")