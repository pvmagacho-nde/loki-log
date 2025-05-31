# loki-log

A simple structured Loki compatible logging utility for Python.

## Overview

`loki-log` provides an easy way to print structured log messages that include useful context such as timestamp, log level, source file and line number, plus optional key-value pairs. This makes logs easier to parse and analyze, especially when ingesting into Loki or similar log aggregation systems.

## Features

- Outputs ISO 8601 UTC timestamps with milliseconds precision.
- Includes log level (`INFO`, `WARN`, `ERROR`, `DEBUG`).
- Automatically captures the source filename and line number where the log call was made.
- Supports optional contextual key-value pairs for richer logs.
- Simple and lightweight, no external dependencies.

## Installation

Clone the repository and install via pip:

```bash
git clone https://github.com/pvmagacho-nde/loki-log.git
cd loki-log
pip install .

