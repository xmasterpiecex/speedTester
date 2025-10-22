#!/usr/bin/env python3
import http.client
import urllib.parse
import time
import sys
import threading

FILE_SIZE_MB = 100
FILE_SIZE_BYTES = FILE_SIZE_MB * 1024 * 1024
CHUNK_SIZE = 409600
THRED_COUND = 16

url = f"https://hel1-speed.hetzner.com/{FILE_SIZE_MB}MB.bin"

def progress_bar(current, total, bar_length=40):
    fraction = current / total
    arrow = '▓' * int(fraction * bar_length)
    padding = '-' * (bar_length - len(arrow))
    end = '\r' if current < total else '\n'
    print(f'Testin speed: |{arrow}{padding}| {int(fraction*100)}%', end=end)
    sys.stdout.flush()

parsed = urllib.parse.urlparse(url)
host = parsed.netloc
path = parsed.path

threadsDownloadedData = [0] * THRED_COUND

def speedTest(index, start, end):
    try:
        conn = http.client.HTTPSConnection(host, timeout=10)
        header = {'Range': f'bytes={start}-{end}'}
        conn.request("GET", path, headers=header)
        respon = conn.getresponse()

        while True:
            chunk = respon.read(CHUNK_SIZE)
            if not chunk:
                break

            threadsDownloadedData[index] += len(chunk)

        conn.close()
    except Exception as err:
        print(err)

def main():
    threads = []
    start = time.perf_counter()
    part_size = FILE_SIZE_BYTES // THRED_COUND
    for i in range(THRED_COUND):
        bstart = i * part_size
        bend =(bstart + part_size - 1) if i != THRED_COUND - 1 else FILE_SIZE_BYTES - 1
        t = threading.Thread(target=speedTest, args=(i, bstart, bend))
        threads.append(t)
        t.start()


    while any(t.is_alive() for t in threads):
        totalDownloadedSize = sum(threadsDownloadedData)
        progress_bar(totalDownloadedSize, FILE_SIZE_BYTES)
        time.sleep(0.1)

    progress_bar(FILE_SIZE_BYTES, FILE_SIZE_BYTES)

    for t in threads:
        t.join()

    end = time.perf_counter()
    totalTime = end - start
    totalDownloadedSize = sum(threadsDownloadedData)
    if totalTime == 0:
        totalTime = 0.0001

    speed_mbps = (totalDownloadedSize*8) / (totalTime * 1000000)
    print(f"Speed test --: {round(speed_mbps)} Mb/sec\n")

if __name__ == "__main__":
    main()
