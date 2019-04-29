## CConf

ISCConf is a library for parsing ISC configuration files, such as `dhcp.conf`
or `named.conf`. It was written, because the existing libraries couldn't
handle some of the constructs that can be commonly encountered in such files in
practice. I took a pragmatic approach, and added things that are not strictly
in the specification, such as unquoted MAC or IP addresses. The goal was to
have something that can parse our own `dhcp.conf` file.


## Usage

There is only one function, ``parse``, that takes a single argument, the string
to be parsed, and returns a data structure consisting of nested lists and
dictionaries, representing the parsed data.

Example:

    import iscconf

    with open("dhcpd.conf", "r") as f:
        data = iscconf.parse(f.read())
