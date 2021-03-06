import os

import riffle


class ExampleSession(riffle.Domain):
    def onJoin(self):
        self.register("echo", self.echo)

    @riffle.want(str)
    def echo(self, msg):
        print("Echo: {}".format(msg))
        return msg


if __name__ == "__main__":
    riffle.SetFabric(os.environ['WS_URL'])
    riffle.SetLogLevelInfo()
    domain = os.environ['DOMAIN']
    ExampleSession(domain).join()
