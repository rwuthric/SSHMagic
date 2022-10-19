"""
IPython magic for executing commands on a remote machine via ssh
"""
# -----------------------------------------------------------------------------
#  Copyright (c) 2022 Rolf Wuthrich, Concordia Univerity
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

from .sshmagic import ssh


def load_ipython_extension(ipython):
    """ Register ssh magics """
    ipython.register_magic_function(ssh, 'cell')
