# Readme

## Description

This is a python application to run specific hardening checks on macOS systems.
It is based industry best practices, and is intended to be used as a tool to conduct security audits.

## Installation

The application should be run as root as it requires root privileges to run some of the checks.
There are no external dependencies, so it should run on any macOS system.

## Usage

The application can be run with the following command:

```python3 compliance.py```

There are no command line arguments, and the application will run all checks by default, the output will be displayed in the terminal
 and also saved to a file called "compliance_report.md" in the same directory as the application.

 ## Checks

A comprehensive list of the checks can be found in the benchmarks directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

Please see LICENSE.md for details.

## Acknowledgements

This application was inspired by the [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/) and the [macOS Sysadmin Conference](https://macsysadmin.se/program/program.html).

