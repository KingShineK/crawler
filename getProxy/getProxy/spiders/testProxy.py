# -*- coding: utf-8 -*-

import re
import threading
import urllib
import urllib.request

class TestProxy(object):
    def __init__(self):
        self.sFile = r'proxy.txt'
        self.dFile = r'alive.txt'
        self.URL = r'www.baidu.com/'
        self.threads = 10
        self.timeout = 3
        self.regex = re.compile(r'baidu.com')
        self.aliveList = []
        self.count = 0

        self.run()

    def run(self):
        with open(self.sFile,'r') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in range(self.threads):
                    t = threading.Thread(target=self.linkWithProxy,args=(line,))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue

        with open(self.dFile,'w') as fp:
            for i in range(len(self.aliveList)):
                fp.write(self.aliveList[i])

    def linkWithProxy(self,line):
        lineList = line.split('\t')
        protocol = lineList[2].lower()
        server = protocol + r'://' + lineList[0] + ':' +lineList[1]
        # print(server)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol:server}))

        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.URL,timeout=self.timeout)
        except:
            print('%s connect failed1' %server)
            self.count = self.count+1
            return
        else:
            try:
                str = response.read()
            except:
                print('%s connect failed2' %server)
                return
            if self.regex.search(str):
                print('%s connect success......' %server)
                self.aliveList.append(line)

if __name__ == '__main__':
    TP = TestProxy()
    print("count:", TP.count)