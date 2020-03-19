from pprint import pprint
from datetime import datetime

def sort_history(log):
   return sorted(log, key=lambda l: l["date"])



def count_sleepy_minutes(log):
    minutes = {}
    for dict in log:
        msg = dict['message']
        date = dict['date']
        msg_split = msg.split(" ")
        if msg.startswith("Guard"):
            id = msg_split[1]
        elif msg.startswith("falls"):
            sleep_start = date.minute
        else:
            if id not in minutes:
                minutes[id] = {i:0 for i in range(60)}
                for j in range(sleep_start, date.minute):
                    minutes[id][j] += 1
            else:
                for j in range(sleep_start, date.minute):
                    minutes[id][j] += 1
    return minutes


def process_input(f):
    log = []
    for line in f:
        message = line[19:]
        date = line[1:17]
        log.append({"date":datetime.strptime(date, '%Y-%m-%d %H:%M'), "message":message.strip('\n')})
    return log

def find_sleepiest_minute(minutes):
    amount = 0
    for id, guard in minutes.items():
        for m, a in guard.items():
            if a>amount:
                minute = m
                amount = a
                sleepy_dude = id
    return sleepy_dude, minute, amount

def main():
    with open("input.txt") as f:
        log = process_input(f)
        sorted_log = sort_history(log)
        minutes = count_sleepy_minutes(sorted_log)
        guard, minute, total = find_sleepiest_minute(minutes)
        print "Sleepiest guard is %s at minute %i for a total amount of %i" %(guard, minute, total)
        print "Guard times minute: %i" % ((int(guard[1:]))*minute)


if __name__ == '__main__':
    main()
