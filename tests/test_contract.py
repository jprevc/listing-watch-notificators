"""
Checks this Plugin against the Core's Plugin interface, through its installed entry points.
"""
from __future__ import annotations

from importlib.metadata import distribution

from listing_watch import registry
from listing_watch.contract import check_plugin

PLUGIN = "listing-watch-notificators"


def test_plugin_meets_the_core_plugin_interface() -> None:
    check_plugin(PLUGIN)


def test_plugin_registers_its_notificators_under_their_existing_names() -> None:
    # Notification Profiles store the Notificator's name, so these names must never change.
    plugins = registry.Registry.from_entry_points(distribution(PLUGIN).entry_points)

    assert plugins.notificator_names() == ["email", "ntfy", "pushover"]
    assert plugins.spider_names() == []
