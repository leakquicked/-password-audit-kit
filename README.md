![Python checks](https://github.com/leakquicked/-password-audit-kit/actions/workflows/python-checks.yml/badge.svg)

# Password Audit Kit

A local-only educational password review helper. It uses simple heuristics and does not store, log or transmit the password.

## Run
Python 3.10+, standard library only.

```bash
python password_audit.py
python -m unittest discover -s tests -v
```

The password is entered through a hidden terminal prompt. Avoid passing real passwords as command-line arguments or testing passwords you currently use; use a unique sample phrase instead.

## Limitations
The entropy figure is a rough illustration based on character categories, not a crack-time estimate. The tool does not check breached-password databases, and it cannot establish whether a password has been reused or exposed. A password manager and unique passwords for every service are recommended. Prefer long, unique passphrases and MFA.

Never paste real credentials into public websites, issue trackers or chat.
