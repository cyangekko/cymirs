#!/bin/python
import sys
import jf_mgr as jfm
import util as ut
from cm_err import *
"""Search, process mir target sites on circles."""

ARG_GENERATE = '-g'
ARG_HELP = '-h'

def print_usage(dest=sys.stderr):
    """Print the usage message to the given file."""
    dest.write('usage:\n')
    dest.write('\tcymirs %s\t\t(generate a template job file)\n'%ARG_GENERATE)
    dest.write('\tcymirs <job>\t\t(run job)\n')
    dest.write('\tcymirs %s\t\t(print this message)\n'%ARG_HELP)

def process_cmdargs(args):
    """Process command line arguments."""
    if len(args) != 2:
        # invalid usage
        return None
    return args[1]

def branch_modes(mode):
    """Branches into the correct program mode."""
    try:
        if mode == ARG_GENERATE:
            return jfm.generate_jf_template()
        elif mode == ARG_HELP:
            print_usage(sys.stdout)
            return 0
        else:
            return run_job(mode) # mode = path to config file, in this case
    except CMErr as cme:
        ut.log.error(str(cme))
    except:
        ut.log.error('Unhandled exception! (ooops)')

if __name__ == '__main__':
    # process args
    mode = process_cmdargs(sys.argv)
    if mode is None:
        ut.log.error('Bad usage.')
        print_usage()
    else:
        sys.exit(branch_modes(mode))