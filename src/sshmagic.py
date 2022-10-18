"""
IPython magic function for executing commands on a remote machine via ssh
"""
# -----------------------------------------------------------------------------
#  Copyright (c) 2022 Rolf Wuthrich, Concordia Univerity
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

import subprocess


def ssh(line, cell):
    """ 
    Executes the cell remotley via ssh

    Usage:

    %%ssh user@remote
    """
    p = subprocess.Popen(f"ssh {line} '{cell}'",
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = p.communicate()
    ans = ret[0].decode("utf8")
    if ret[1]:
        print(f"\x1b[31m{ret[1].decode('utf8')}\x1b[0m")
    return print(ans)


def load_ipython_extension(ipython):
    """ Register ssh magics """
    ipython.register_magic_function(ssh, 'cell')
