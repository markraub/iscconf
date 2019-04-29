import unittest
import iscconf


class TestDHCPParsing(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_empty(self):
        data = iscconf.parse('')
        self.assertEqual(data, {})

    def test_empty_comment(self):
        data = iscconf.parse('# xxx')
        self.assertEqual(data, {})

    def test_mac_2e(self):
        data = iscconf.parse("2e:2c:45:e8:c9:23;")
        self.assertEqual(data, {
            (): '2e:2c:45:e8:c9:23',
        })

    def test_mac_2E(self):
        data = iscconf.parse("2E:2C:45:E8:C9:23;")
        self.assertEqual(data, {
            (): '2e:2c:45:e8:c9:23',
        })

    def test_single(self):
        data = iscconf.parse("""\
host s10557.dc2 {
    fixed-address 10.242.15.6;
    hardware ethernet 00:1b:78:cf:b3:90;
}""")
        self.assertEqual(data, {
            ('host', 's10557.dc2'): {
                    ('fixed-address',): '10.242.15.6',
                    ('hardware', 'ethernet'): '00:1b:78:cf:b3:90',
                },
        })

    def test_list(self):
        data = iscconf.parse("""\
host s10557.dc2 {
    fixed-address 10.242.15.6, 127.0.0.1;
    hardware ethernet 00:1b:78:cf:b3:90;
}""")
        self.assertEqual(data, {
            ('host', 's10557.dc2'): {
                    ('fixed-address',): ['10.242.15.6', '127.0.0.1'],
                    ('hardware', 'ethernet'): '00:1b:78:cf:b3:90',
                },
        })

    def test_single_comments(self):
        data = iscconf.parse("""\
# comment
host s10557.dc2 {
# comment
    fixed-address 10.242.15.6;
    hardware ethernet 00:1b:78:cf:b3:90;
}
# comment
""")
        self.assertEqual(data, {
            ('host', 's10557.dc2'): {
                    ('fixed-address',): '10.242.15.6',
                    ('hardware', 'ethernet'): '00:1b:78:cf:b3:90',
                },
        })

    def test_multi(self):
        data = iscconf.parse("""\
host s10557.dc2 {
    fixed-address 10.242.15.6;
    hardware ethernet 00:1b:78:cf:b3:90;
}
host s10498.dc2 { fixed-address 10.242.15.5;
hardware ethernet 00:1a:4b:d0:7c:60; }""")
        self.assertEqual(data, {
            ('host', 's10557.dc2'): {
                    ('fixed-address',): '10.242.15.6',
                    ('hardware', 'ethernet'): '00:1b:78:cf:b3:90',
                },
            ('host', 's10498.dc2'): {
                    ('fixed-address',): '10.242.15.5',
                    ('hardware', 'ethernet'): '00:1a:4b:d0:7c:60',
                },
        })

    def test_string(self):
        data = iscconf.parse("""\
xxx {
    xxx "hello world";
}""")
        self.assertEqual(data, {
            ('xxx',): {
                ('xxx',): 'hello world',
            },
        })

    def test_no_key(self):
        data = iscconf.parse("""allow-query { "none"; };""")
        self.assertEqual(data, {
            ('allow-query',): {(): 'none'},
        })

    def test_listen(self):
        data = iscconf.parse("""listen-on port 1053 { "any"; };""")
        self.assertEqual(data, {
            ('listen-on', 'port', 1053): {(): 'any'},
        })


if __name__ == '__main__':
    unittest.main()
