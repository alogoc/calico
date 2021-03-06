Welcome to Calico
=================

Project Calico is an open source solution for virtual networking in
cloud data centers, developed by `Metaswitch
Networks <http://www.metaswitch.com/>`__ and released under the `Apache
2.0
License <https://github.com/Metaswitch/calico-docs/blob/master/LICENSE.txt>`__.
You can find more information about it on `our
website <http://www.projectcalico.org/>`__.

Architecture
------------

Calico represents a new approach to virtual networking, based on the
same scalable IP networking principles as the Internet. See :doc:`arch-overview`
for an overview of how Calico works and what a Calico deployment
contains.

Getting Started
---------------

-  :doc:`opens-install-inst`
-  :doc:`verification`

Getting Source Code
-------------------

All of the source code is on `GitHub <https://github.com/Metaswitch>`__,
in the following repositories, separated by function

Product Code
~~~~~~~~~~~~

-  `calico <https://github.com/Metaswitch/calico>`__ - the Felix agent,
   the ACL manager, and the officially-supported orchestrator plugins.
-  `calico-neutron <https://github.com/Metaswitch/calico-neutron>`__ -
   Calico-specific patched version of OpenStack Neutron.
-  `calico-nova <https://github.com/Metaswitch/calico-nova>`__ -
   Calico-specific patched version of OpenStack Nova.
-  `calico-dnsmasq <https://github.com/Metaswitch/calico-dnsmasq>`__ -
   Calico-specific patched version of dnsmasq.

Infrastructure
~~~~~~~~~~~~~~

-  `calico-chef <https://github.com/Metaswitch/calico-chef>`__ - Chef
   cookbooks for installing test versions of OpenStack-using-Calico.

Contributing
------------

You can contribute by making a GitHub pull request. See :doc:`contribute` 
for details.

Support
-------

If you want help or to help others, check out :doc:`support`.

License and Acknowledgements
----------------------------

Calico's license is documented in
`LICENSE.txt <https://github.com/Metaswitch/calico-docs/blob/master/LICENSE.txt>`__.

It also makes use of other open source components as acknowledged in
`README.txt <https://github.com/Metaswitch/calico-docs/blob/master/README.txt>`__.
