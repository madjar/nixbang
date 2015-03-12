Nixbang
=======

Nixbang let you specify the dependencies of a script inside the script itself. It will then use nix-shell to run the script with the dependenies. This has two advantages :

 - the dependencies do not clutter the system (thanks to the magic of nix) ;
 - the script can be executed on any system without setting up
   anything but nixbang (and nix).

Example
-------

Take the following script ::

  #!/usr/bin/env nixbang
  # command = python3
  # packages = python34 python34Packages.requests tree

  import requests
  print(requests)
  import subprocess
  subprocess.call(['tree'])

Making it executable and running it with get all the dependencies
specified on the `packages` line, and run the script in an environment
with all those dependencies, with the command specified in `command`.

Note that the dependencies can be any nixpkgs packages, meaning a
python script can specify both python dependencies and commands it
would like to use.


Usage
-----

Set the beginning of you script to look like this ::

  #!/usr/bin/env nixbang
  # command = python3
  # packages = python34 python34Packages.requests tree

The `command` line tells which command should be used to execute the
script. It plays the same role as the usual shebang.

The `packages` line tells which dependencies are required to run the
script. Remember to add the command itself!

Note
----

Something similar has been implemented in nix-shell since, so you might want to take a look at it : https://github.com/NixOS/nix/commit/a957893b261a4438101c205e38fe8ce62b83a121.
