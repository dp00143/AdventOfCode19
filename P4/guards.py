from pprint import pprint
from datetime import datetime

def sort_history(log):
   return sorted(log, key=lambda l: l["date"])

def find_sleepiest_guard(sorted_log):
    sleep_ratio = {}
    for dict in sorted_log:
        msg = dict['message']
        date = dict['date']
        msg_split = msg.split(" ")
        if msg.startswith("Guard"):
            id = msg_split[1]
        elif msg.startswith("falls"):
            sleep_start = date.minute
        else:
            assert msg.startswith("wakes")
            if id in sleep_ratio:
                sleep_ratio[id] += date.minute - sleep_start
            else:
                sleep_ratio[id] = date.minute - sleep_start
    sleep_order = sorted(sleep_ratio, key=sleep_ratio.__getitem__)
    guard = sleep_order[-1]
    minutes_asleep = sleep_ratio[guard]
    return guard, minutes_asleep


def find_sleepiest_minute(guard, log):
    minutes = {i:0 for i in range(60)}
    for dict in log:
        msg = dict['message']
        date = dict['date']
        msg_split = msg.split(" ")
        if msg.startswith("Guard"):
            id = msg_split[1]
        elif msg.startswith("falls") and id==guard:
            sleep_start = date.minute
        elif msg.startswith("wakes") and id==guard:
            for j in range(sleep_start, date.minute):
                minutes[j] += 1
    minutes_order = sorted(minutes, key=minutes.__getitem__)
    minute = minutes_order[-1]
    total = minutes[minute]
    return minute, total


def process_input(f):
    log = []
    for line in f:
        message = line[19:]
        date = line[1:17]
        log.append({"date":datetime.strptime(date, '%Y-%m-%d %H:%M'), "message":message.strip('\n')})
    return log

def main():
    with open("input.txt") as f:
        log = process_input(f)
        sorted_log = sort_history(log)
        guard, total_minutes = find_sleepiest_guard(sorted_log)
        minute, total = find_sleepiest_minute(guard, sorted_log)
        print "Guard %s is asleep %i minutes total and is sleepiest at minute %i" % (guard, total_minutes, minute)
        print "Guard id times minute: %i" % ((int(guard[1:]))*minute)


if __name__ == '__main__':
    main()
