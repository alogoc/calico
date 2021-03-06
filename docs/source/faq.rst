Frequently Asked Questions
==========================

This page contains answers to several frequently asked technical
questions about Project Calico. It is updated on a regular basis: please
check back for more information.

"How Does Calico Maintain Saved State?"
---------------------------------------

State is saved in a few places in a Calico deployment, depending on
whether it's global or local state.

Local state is state that belongs on a single compute host (associated
with a single running Felix instance). That state is actually entirely
stored by the Linux kernel on that host: Felix doesn't store any of it
internally. This makes Felix basically stateless, with the kernel acting
as a backing data store on one side and the plugin/ACL manger as a data
source on the other.

If Felix dies and returns, it learns current state from the kernel
(things like kernel routes, tap devices etc.) at start up. It then asks
the plugin for a full report of the state it should have, and updates
the kernel to match. This approach has strong resiliency benefits, in
that if Felix crashes you don't suddenly lose access to your VMs. As
long as the Linux kernel is running, you've still got functionality.

The bulk of global state is mastered in whatever component hosts the
plugin. In the case of OpenStack, this means a Neutron database. Our
OpenStack plugin (more strictly a Neutron ML2 driver) queries the
Neutron database to find out state about the entire deployment. That
state is then reflected down to Felix and the ACL manager. In other
orchestration systems, it may be stored in distributed databases, either
owned directly by the plugin or by the orchestrator itself.

The only other state storage in a Calico network is in the BGP sessions,
which approximate a distributed database of routes. This isn't actually
the master state (that's stored by the orchestrator), but it's the state
that is updated by Calico in response to changes in the master state.

This makes the Calico design very simple, because we store very little
state. All of our components can be shutdown and restarted without risk,
because they resynchronize state as necessary. This makes modelling
their behaviour extremely simple, reducing the complexity of bugs.
