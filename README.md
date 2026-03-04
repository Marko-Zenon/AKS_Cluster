# Radxa Q6A: Edge Computing & System Integration Project
This project focuses on the configuration, optimization, and development environment setup for the Radxa Q6A single-board computer. It covers a wide range of engineering tasks, from Linux system administration and networking to high-performance C++ computing and autonomous AI agents.

**Key Development Areas**
High-Performance Computing: Developing C++ applications for double integral calculations using multi-threading and parallel computing techniques.

Performance Benchmarking: Analyzing I/O operation speeds and string-to-number conversion methods to optimize data processing.

Autonomous Systems: Developing a Telegram bot powered by a custom-trained language model for real-time monitoring and interaction.

Digital Logic & Hardware: Designing a 2-bit ALU and working with shift registers and microcontrollers.

**Networking & Connection (Windows Setup)**
Since the project often requires a direct "point-to-point" Ethernet connection without a router, the following setup is used:

- Internet Connection Sharing (ICS)
To provide the Radxa Q6A with internet access through your laptop:

Open Control Panel -> Network and Sharing Center.

Go to Change adapter settings.

Right-click your active Wi-Fi -> Properties -> Sharing tab.

Check "Allow other network users to connect through this computer's Internet connection" and select the Ethernet port.

Windows will assign the IP 192.168.137.1 to your PC.

- Identifying Radxa's IP
After connecting the cable, locate the board's IP address using the Windows terminal:

```Bash
arp -a
```

Look for an address in the 192.168.137.x range (e.g., 192.168.137.5 or 192.168.137.74).

**Working in the System**
SSH Access
Connect to the board via terminal:

```Bash
ssh radxa@<YOUR_IP>
Password: radxa
```

Session Management with tmux
To keep your sessions alive even if the Ethernet connection drops, use tmux:

```Bash
tmux
```

Ctrl + B, then % — Split the window vertically.

System Monitoring
Use btop for a real-time visual dashboard of CPU, RAM, and network usage:

```Bash
btop
```

**System Optimization (Disabling Sleep)**
To prevent connection drops during long-running tasks (like C++ compilations or bot hosting), sleep modes are disabled on the Radxa:

```Bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

Additionally, it is recommended to disable "Allow the computer to turn off this device to save power" for the Ethernet adapter in the Windows Device Manager.

**Roadmap**
Computer Vision: Implementing Homography and OpenCV-based image processing.

Database Integration: Deploying a database for the "Books" domain project.

Static IP Configuration: Setting a permanent IP to bypass frequent arp -a checks.
