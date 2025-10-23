# 🧪 Python CLI Speed Test Tool

---[Screencast_20251023_215144.webm](https://github.com/user-attachments/assets/b948f919-758b-49ac-ae4d-34ab342702dc)

> [!WARNING] :
> This project only for Unix base os.

A lightweight, multithreaded internet download speed test written in pure Python.

This tool downloads a test file from a remote server using multiple threads and calculates your approximate download speed in Mbps.




## 🚀 Features

- ✅ Written in pure Python — no external dependencies
- ✅ Uses `http.client` for direct HTTPS connections
- ✅ Multithreaded download to simulate real-world usage
- ✅ Live terminal progress bar
- ✅ Accurate Mbps speed result
- ✅ Easy to use from terminal

---

## 🛠️ How It Works

- Connects to a remote test server
- Divides a large file into chunks
- Launches multiple threads to download separate byte ranges in parallel
- Measures time taken and total data received
- Calculates and displays approximate download speed in Mbps

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-speedtest.git
cd python-speedtest
```

## Usage

```bash
python3 speedtest.py
```
