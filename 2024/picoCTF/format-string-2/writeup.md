# format-string-2

On first glance of this problem, we can see that we need to overwrite `sus` to
be `0x67616c66` which is `galf` in hex. This is done using the insecure printf
and writing data to `sus`.

In order to do this, we need to utilize %n. The `solve.py` script includes
an example of how to do this, taken from the [pwntools example](https://docs.pwntools.com/en/stable/fmtstr.html).
