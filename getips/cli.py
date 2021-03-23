import click
import socket
import os

class colors:
    INFO = '\033[94m' + '[INF]: '
    WARNING = '\033[93m' + '[WAR]: '
    FAIL = '\033[91m' + '[ERR]: '
    BOLD = '\033[1m'
    OKGREEN = '\033[92m' + '[OK]: '


def identity(x):
    return x

@click.command()
@click.option("--domains", "-d", "in_file", required=True, help="Path for file with domains.")
@click.option("--output", "-o", "out_file", help="Path for output file with list of IPs.")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output.")
def process(in_file, out_file, verbose):
    """ Process the input file IN and store result to file OUT, 
    or print in output.
    """

    print_func = print if verbose else identity

    try:
        hosts = open(in_file, 'r')
        lines = hosts.readlines()
    except:
        print_func(colors.FAIL + "Program is unable to read input file.")
        exit()

    ips = []
    count = 0
    for line in lines:
        host = line.strip()
        count += 1
        try:
            ip = socket.gethostbyname(host)
        except:
            print_func(colors.WARNING + "Host: %s is not available." % (host))

        print_func(colors.INFO + "Host: %s has an IP: %s" % (host, ip))
        ips.append(ip + os.linesep)

    if out_file:
        output_lines = sorted(set(ips))

        output = open(out_file, 'w')
        output.writelines(output_lines)
        output.close()
    else:
        print(colors.OKGREEN + "Execution finished.")
        for ip in ips:
            print(ip.strip())

def main():
    print("\n")
    print("\n")
    print(" @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@    @@@@@@   ")
    print("@@@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@@@@@   ")
    print("!@@        @@!         @@!    @@!  @@!  @@@  !@@       ")
    print("!@!        !@!         !@!    !@!  !@!  @!@  !@!       ")
    print("!@! @!@!@  @!!!:!      @!!    !!@  @!@@!@!   !!@@!!    ")
    print("!!! !!@!!  !!!!!:      !!!    !!!  !!@!!!     !!@!!!   ")
    print(":!!   !!:  !!:         !!:    !!:  !!:            !:!  ")
    print(":!:   !::  :!:         :!:    :!:  :!:           !:!   ")
    print(" ::: ::::   :: ::::     ::     ::   ::       :::: ::   ")
    print(" :: :: :   : :: ::      :     :     :        :: : :    ")
    print("\n")
    print("\n")
    print(colors.BOLD + "Welcome to getIPs v0.1.1 by @_n4Zz2_")
    print("\n")

    process()