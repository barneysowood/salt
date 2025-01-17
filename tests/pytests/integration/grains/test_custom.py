"""
Test the custom grains
"""

from pprint import pprint

import pytest

pytestmark = [
    pytest.mark.windows_whitelisted,
    pytest.mark.slow_test,
]


def test_show_fileserver(salt_call_cli):
    """
    Check config
    """
    ret_roots = salt_call_cli.run("config.get", "file_roots")
    assert ret_roots.returncode == 0
    pprint(ret_roots.data["base"])
    ret_list_master = salt_call_cli.run("cp.list_master")
    assert ret_list_master.returncode == 0
    pprint(ret_list_master.stdout)
    assert False


def test_grains_passed_to_custom_grain(salt_call_cli):
    """
    test if current grains are passed to grains module functions that have a grains argument
    """
    ret = salt_call_cli.run("grains.item", "custom_grain_test")
    assert ret.returncode == 0
    assert ret.data
    assert ret.data["custom_grain_test"] == "itworked"
