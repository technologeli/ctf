# heap 0

This one was pretty easy. When we call write_buffer(), it scans as much into
input_data as we want, even though it is only 5 bytes.
Therefore we can overwrite it by sending a really long string of anything
and the safe_var, which is allocated immediately after.
