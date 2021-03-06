import sys
import os
import subprocess as ssubprocess


_p = None


def start_syslog():
    global _p
    _p = ssubprocess.Popen(['logger',
                            '-p', 'local2.notice',
                            '-t', 'sshuttle', '-i'], stdin=ssubprocess.PIPE)


def stderr_to_syslog():
    sys.stdout.flush()
    sys.stderr.flush()
    os.dup2(_p.stdin.fileno(), 2)
