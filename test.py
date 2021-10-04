import psutil
import platform
import os
import sys
from time import sleep
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

while True:
    stdscr.addstr(3, 5,"="*32+ "CPU Info"+ "="*32,curses.A_NORMAL)
    stdscr.addstr(4, 5, "Total CPU Usage: "+ str(psutil.cpu_percent()) + " %", curses.A_NORMAL)
    stdscr.addstr(5, 5, "CPU Usage Per Core:",curses.A_NORMAL)
    max = 0
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        stdscr.addstr(i+6, 5,"Core "+ str(i) +": " + str(percentage) + " %", curses.A_NORMAL)
        if(i+6 > max):
            max = i+6
    stdscr.addstr(max, 5, "="*28+ "Memory Information"+ "="*28,curses.A_NORMAL)
    svmem = psutil.virtual_memory()
    max += 1
    stdscr.addstr(max, 5, "Total: " + str(get_size(svmem.total)),curses.A_NORMAL)
    max += 1
    stdscr.addstr(max, 5, "Available: " + str(get_size(svmem.available)),curses.A_NORMAL)
    max += 1
    stdscr.addstr(max, 5, "Used: " + str(get_size(svmem.used)),curses.A_NORMAL)
    max += 1
    stdscr.addstr(max, 5, "Percentage: " + str(svmem.percent) + " %",curses.A_NORMAL)
    # print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    #
    # print("CPU Usage Per Core:")
    # for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    #     print(f"Core {i}: {percentage}%")
    #
    #
    #
    # print("="*40, "Memory Information", "="*40)
    # svmem = psutil.virtual_memory()
    # print(f"Total: {get_size(svmem.total)}")
    # print(f"Available: {get_size(svmem.available)}")
    # print(f"Used: {get_size(svmem.used)}")
    # print(f"Percentage: {svmem.percent}%")
    stdscr.refresh()
    sleep(1)
