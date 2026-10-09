# Listing Watch Notificators

[![Tests](https://github.com/jprevc/listing-watch-notificators/actions/workflows/main.yml/badge.svg)](https://github.com/jprevc/listing-watch-notificators/actions/workflows/main.yml)
[![PyPI version](https://badge.fury.io/py/listing-watch-notificators.svg)](https://pypi.org/project/listing-watch-notificators/)

A [Listing Watch](https://github.com/jprevc/listing-watch) Plugin that provides three Notificators:
**Email** (Gmail SMTP), **Pushover** and **ntfy**. Install it next to the Core and they appear in the
Notification Profile form; the Core's public Docker image already includes it.

```bash
pip install "listing-watch-notificators>=1,<2"
```

It depends on `listing-watch>=4,<5` and registers its Notificators under the
`listing_watch.notificators` entry-point group, as `email`, `pushover` and `ntfy`.

## Email

1. Create an [App Password](https://myaccount.google.com/apppasswords) for your Gmail account.
2. Enter the username and password into an email notification profile.

## Pushover

1. Sign up at [Pushover](https://pushover.net/signup) and note your **user token**.
2. Register your app at [Pushover Apps](https://pushover.net/apps/build) and get an **API token**.
3. Enter the user token(s) and API token into a Pushover notification profile.
4. Install the [Pushover app](https://pushover.net/) on your device(s) to receive notifications.

Trial expires after 30 days; a one-time purchase is required to continue. See [Pushover pricing](https://pushover.net/pricing).

- [Android](https://play.google.com/store/apps/details?id=net.superblock.pushover)
- [App Store](https://apps.apple.com/us/app/pushover-notifications/id506088175)

## ntfy

1. Pick a topic name (a unique, unguessable string) on the public [ntfy.sh](https://ntfy.sh/) service, or run your own [self-hosted ntfy server](https://docs.ntfy.sh/install/).
2. Subscribe to that topic in the [ntfy app](https://ntfy.sh/#subscribe) (Android/iOS/web) or CLI to receive notifications.
3. Configure the notification profile with `topic` (required), and optionally `server` (defaults to `https://ntfy.sh`), `priority`, `tags`, and authentication (`token`, or `username`+`password` for a protected topic/self-hosted server).

## Development

```bash
uv sync
uv run pytest
```

The tests include the Core's Plugin contract check (`listing_watch.contract.check_plugin`).
