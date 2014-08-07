# Copyright (c) 2014 Pica8, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paramiko
from oslo.config import cfg
from neutron.openstack.common import log as logging

LOG = logging.getLogger(__name__)

CONFIG = [
               cfg.StrOpt('switches', default='',
                          help=_('The info of the switches to SSH to')),
               cfg.StrOpt('commands', default='',
                          help=_('The commands to run on the switches')),
         ]

cfg.CONF.register_opts(CONFIG, "ml2_pica8")

class Pica8Driver():
    """ML2 mechanism driver for PicOS enabled hardware switches
    """

    def __init__(self):
        pass

    def initialize(self):
        self.config = {'switches': cfg.CONF.ml2_pica8.switches,
                       'commands': cfg.CONF.ml2_pica8.commands
                      }
        switchlist = self.config['switches'].replace('\n','').split(';')
        commands = self.config['commands'].replace('\n','')
        for sw in switchlist:
            username = sw.split(':')[0]
            password = sw.split(':')[1].split('@')[0]
            host = sw.split('@')[1]
            self.execute_commands(host, username, password, commands)

    def execute_commands(self, host, username, password, commands):
        LOG.info(_('Executing commands on switch %s') % host)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            #print "creating connection to " + host
            ssh.connect(host, username=username, password=password, timeout=5)
            #print "connected"
            stdin, stdout, stderr = ssh.exec_command(commands, timeout=10)
            #for line in stdout:
            #    print '... ' + line.strip('\n')
        finally:
            #print "closing connection to " + host
            ssh.close()
            #print "closed"

