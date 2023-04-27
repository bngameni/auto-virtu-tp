#!/usr/bin/env python
import sys

def test_apache_service_is_running(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

def test_users_is_created(host):
    for user in ("delibes","del"):
        assert host.user(user).exists


def test_ntp_service(host):
    if 'debian' in sys.platform.lower():
        ntp_file = host.file("/etc/ntp.conf")
        assert host.service("ntp").is_running
        assert ntp_file.contains("time.google.com")
