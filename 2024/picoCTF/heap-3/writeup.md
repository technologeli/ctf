# heap-3

This heap problem just shows the problems with not setting pointers to null after
freeing. Because allocation of an object immediately after freeing may give the
same pointer, we can write to old pointers.

I previously thought this was a double free vulnerability, but it was much simpler.
