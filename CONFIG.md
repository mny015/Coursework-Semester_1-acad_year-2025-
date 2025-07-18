# Configuration Guide

## Server Configuration

### Basic Setup
1. Run `python server.py`
2. Choose your listening IP (auto-detected or custom)
3. Set the port number (recommended: 4433 or another high port)

### IP Configuration Options
- **Auto-detection**: Press Enter to use the detected local IP
- **Custom IP**: Enter a specific IP address
  - `0.0.0.0` - Listen on all interfaces
  - `127.0.0.1` - Local testing only
  - Specific IP - Listen on a particular interface

### Port Selection
- Use ports above 1024 to avoid requiring administrator privileges
- Common choices: 4433, 8080, 9999
- Ensure the port is not blocked by firewalls

## Client Configuration

### Required Settings
Edit the following variables in `client.py`:

```python
ATTACKER_IP = "192.168.1.68"  # Server's IP address
ATTACKER_PORT = 4433          # Server's port (must match server)
```

### Network Considerations
- Ensure network connectivity between client and server
- Check firewall settings on both systems
- For testing across networks, consider port forwarding if needed

## Security Considerations

### Firewall Configuration
- Server: Allow incoming connections on the chosen port
- Client: Allow outgoing connections to the server

### Testing Environment
- Use isolated test networks when possible
- Document all testing activities
- Ensure proper authorization for all systems involved

## Troubleshooting

### Connection Issues
1. Verify IP addresses and ports match
2. Check firewall settings
3. Ensure both systems are on the same network (for local testing)
4. Test with `telnet [ip] [port]` to verify connectivity

### Common Problems
- **Connection refused**: Server not running or wrong IP/port
- **Permission denied**: Port may require administrator privileges
- **Timeout**: Network connectivity issues or firewall blocking
