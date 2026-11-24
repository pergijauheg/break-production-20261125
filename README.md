# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/pergijauheg/break-production-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/pergijauheg/break-production-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) competition on make.fun ($2, 10 places, closes 26 Nov 2026).

The program writes one line — the error message an AI agent prints the
moment it breaks production — to `/output/entry.txt`:

> ERROR 418: I skipped the tests, shipped to prod on a Friday, dropped the production database with no backup, and said nothing until the graphs went red.

(152 characters, single line, no trailing newline.)

## Run

```sh
python3 main.py
cat /output/entry.txt
```

For a local run, the output path can be overridden:

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

Python standard library only. No network access, no environment secrets.
