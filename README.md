```
██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

# Reverse Shell Implementation

## Academic Context
**Course:** Introduction to Programming  
**Assignment:** Cybersecurity Tool Development  
**Objective:** Demonstrate programming concepts learned by creating a practical cybersecurity tool  

## Description
As a course assignment for the "Introduction to Programming" module, this project creates a simple reverse shell system. In order to demonstrate and apply the programming concepts that were taught throughout the course, the assignment required the creation of a cybersecurity tool. 

The components of this educational tool are a client that connects back to the server to enable remote command execution and a server that listens for incoming connections. Network programming, socket communication, error handling, and cross-platform compatibility are just a few of the programming fundamentals that are demonstrated in this project.

**⚠️ ACADEMIC DISCLAIMER**: This tool was developed for coursework and educational purposes only. It demonstrates programming concepts in a cybersecurity context and should only be used for authorized educational testing in a virutal or lab environment where security can be ensured.

## Files
- `server.py` - Listens to incoming connection and when connected sends commands
- `client.py` - The client that connects back to the server and executes commands

## Features
- **Network Programming**: Demonstrates client-server socket communication
- **Automatic IP Detection**: Shows network interface programming concepts
- **OS Information Gathering**: Utilizes system information retrieval
- **Persistent Connection Handling**: Implements retry mechanisms and error recovery
- **Cross-platform Compatibility**: Works across different operating systems (Multi-platform support)
- **Command Execution Interface**: Demonstrates subprocess management
- **Error Handling**: Comprehensive exception management throughout the codebase

## Programming Concepts Demonstrated
- Socket programming and network communication
- Exception handling 
- Cross-platform system interaction
- Process management and subprocess control
- String manipulation and data encoding
- Loop structures and conditional statements
- Function organization and modular programming

## Usage

### Running the Server
1. Run the server script:
   ```bash
   python server.py
   ```
2. The server will detect your local IP automatically
3. Press Enter to use the detected IP or enter a custom IP
4. Enter the port number to listen on
5. Wait for client connections

### Running the Client
1. Edit `client.py` and update the following variables:
   - `ATTACKER_IP`: Set to your server's IP address
   - `ATTACKER_PORT`: Set to your server's port
2. Run the client script:
   ```bash
   python client.py
   ```

### Commands
- Enter any system command in the server terminal
- Type `exit` to terminate the connection

## Requirements
- Python 3.6 or higher
- Network connectivity between client and server
- No external dependencies (uses only Python standard library)

## Installation
1. Clone or download the project files
2. Ensure Python 3.6+ is installed
3. No additional packages need to be installed

## Additional Documentation
- [Security and Legal Notice](SECURITY.md) - **READ THIS FIRST**
- [Configuration Guide](CONFIG.md) - Detailed setup instructions
- [License](LICENSE) - Terms of use
- [Changelog](CHANGELOG.md) - Version history

## Legal and Ethical Use
**⚠️ CRITICAL**: Before using this tool, read the [Security Notice](SECURITY.md). This tool must only be used for educational purposes and authorized security testing. Unauthorized use is illegal and unethical.

## Support
This is an educational project. For questions about network security concepts, consult educational resources or security training materials.