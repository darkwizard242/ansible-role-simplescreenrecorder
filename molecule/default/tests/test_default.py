import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_simplescreenrecorder_package_installed(host):
    assert host.package("simplescreenrecorder").is_installed


def test_simplescreenrecorder_binary_exists(host):
    assert host.file('/usr/bin/simplescreenrecorder').exists


def test_simplescreenrecorder_binary_file(host):
    assert host.file('/usr/bin/simplescreenrecorder').is_file


def test_simplescreenrecorder_binary_which(host):
    assert host.check_output('which simplescreenrecorder') == \
      '/usr/bin/simplescreenrecorder'
