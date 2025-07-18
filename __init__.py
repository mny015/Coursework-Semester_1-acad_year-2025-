#!/usr/bin/env python3
"""
Reverse Shell Security Testing Tool
==================================

A simple reverse shell implementation for educational purposes and authorized 
security testing. This tool demonstrates basic network communication and 
remote command execution concepts.

IMPORTANT: This tool should only be used for:
- Educational purposes
- Authorized penetration testing
- Security research on systems you own
- Legitimate security assessments with proper authorization

Author: Security Research
License: Educational Use Only
"""

__version__ = "1.0.0"
__author__ = "Security Research"
__license__ = "Educational Use Only"

import sys

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        sys.exit(1)

def main():
    """Main entry point for the package."""
    check_python_version()
    print("Reverse Shell Tool v" + __version__)
    print("Use 'python server.py' to start the server")
    print("Use 'python client.py' to start the client")

if __name__ == "__main__":
    main()
