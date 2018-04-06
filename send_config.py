import argparse
import sys
from ncclient import manager
from lxml import etree

USER = 'admin'
PASSWD = 'admin'
PORT = 5533
HOST = 'localhost'


def main():
    parser = argparse.ArgumentParser(description="send XML file to the\
                                                  switch via NETCONF")
    parser.add_argument('-i', '--input', help='XML file name',
                        dest='xml_file', required=True)
    args = parser.parse_args()
    with manager.connect(host=HOST, port=PORT, username=USER, password=PASSWD,
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         look_for_keys=False, allow_agent=False) as mc:
        with open(args.xml_file, 'r') as fh:
            myconfig = fh.read()
        try:
            netconf_response = mc.edit_config(target='running', config=myconfig, default_operation='merge')
            print netconf_response
        except Exception as err:
            print err


if __name__ == '__main__':
    sys.exit(main())
