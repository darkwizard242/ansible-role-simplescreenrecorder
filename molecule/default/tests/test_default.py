import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'simplescreenrecorder'
PACKAGE_BINARY = '/usr/bin/simplescreenrecorder'


def test_simplescreenrecorder_package_installed(host):
    """
    Tests if simplescreenrecorder is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_serverspec_binary_exists(host):
    """
    Tests if simplescreenrecorder binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_serverspec_binary_file(host):
    """
    Tests if simplescreenrecorder binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_serverspec_binary_which(host):
    """
    Tests the output to confirm simplescreenrecorder's binary location.
    """
    assert host.check_output('which simplescreenrecorder') == PACKAGE_BINARY
