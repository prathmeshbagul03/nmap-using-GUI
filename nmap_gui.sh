#!/bin/bash

# Welcome message
echo "Welcome to the Nmap Easy Interface!"
echo "This tool will guide you through using Nmap without needing to remember commands."

# Ask the user for the target IP or hostname
read -p "Enter the target IP or hostname: " target

# Display scan options
echo "Please select a scan type:"
echo "1) Ping Scan (Discover live hosts)"
echo "2) TCP SYN Scan (Stealthy scan)"
echo "3) TCP Connect Scan (Complete connection)"
echo "4) UDP Scan (Scan UDP ports)"
echo "5) OS Detection (Detect the target's OS)"
echo "6) Version Detection (Detect service versions)"
echo "7) Aggressive Scan (Enable OS detection, version detection, script scanning, and traceroute)"
echo "8) Full Scan (Scan all 65535 ports)"
echo "9) Custom Scan (Enter your own Nmap options)"

# Get the user's choice
read -p "Enter the number of your choice: " choice

# Run the selected scan
case $choice in
    1)
        echo "Running Ping Scan..."
        nmap -sn $target
        ;;
    2)
        echo "Running TCP SYN Scan..."
        nmap -sS $target
        ;;
    3)
        echo "Running TCP Connect Scan..."
        nmap -sT $target
        ;;
    4)
        echo "Running UDP Scan..."
        nmap -sU $target
        ;;
    5)
        echo "Running OS Detection..."
        nmap -O $target
        ;;
    6)
        echo "Running Version Detection..."
        nmap -sV $target
        ;;
    7)
        echo "Running Aggressive Scan..."
        nmap -A $target
        ;;
    8)
        echo "Running Full Scan..."
        nmap -p- $target
        ;;
    9)
        read -p "Enter your custom Nmap options: " custom_options
        echo "Running Custom Scan..."
        nmap $custom_options $target
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo "Scan complete!"
