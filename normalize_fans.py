#!/usr/bin/env python

import re
import sys
import time
import argparse

def write_command(command):
    with open('/proc/acpi/call', 'w') as acpi_call:
        acpi_call.write(command)
        acpi_call.close()
        
def read_command(command):
    write_command(command)
    with open('/proc/acpi/call', 'r') as acpi_call:
        result = acpi_call.read()
        acpi_call.close()
    return result

def write_ec_memory(memory, value):
    command = '\_SB.PCI0.LPCB.EC0.WRAM {} {}'.format(hex(memory), hex(value))
    write_command(command)

def read_ec_memory(memory):
    command = '\_SB.PCI0.LPCB.EC0.RRAM {}'.format(hex(memory))
    result = read_command(command)
    return int(result.split('\x00')[0], 16)

def fit_memory(mem):
  value = read_ec_memory(mem)
  value = value & 0xBF
  write_ec_memory(mem, value)
        
def main():
	fit_memory(0x521)
	fit_memory(0x522)
	
        
if __name__ == '__main__':
	main()
