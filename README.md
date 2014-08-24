Openstack-Neutron
=================

OpenStack Neutron ML2 Driver for Pica8 Switches


The Pica8 Neutron plug-in package includes:

1. entry_points.txt
This file should be copied to the <python lib>/neutron-2014.1.1-py2.7.egg-info/, e.g., /usr/lib/python2.7/site-packages/neutron-2014.1.1-py2.7.egg-info/.
2. ml2_conf_pica8.ini The file should be located in /etc/neutron/plugins/ml2/.
3. ml2_conf.ini The file should be updated with 'mechanism_drivers = openvswitch,pica8'.
The file should be located in /etc/neutron/plugins/ml2/.
4. <dir> pica8 The directory and it files should be copied to  <python lib>/neutron/plugins/ml2/drivers/.

To run the neutron-server with the plug-in, use:
/usr/bin/neutron-server --config-file /usr/share/neutron/neutron-dist.conf --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugin.ini --config-file /etc/neutron/plugins/ml2/ml2_conf_pica8.ini  --log-file /var/log/neutron/server.log

