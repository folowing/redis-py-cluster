import sys
import time
import logging.config
from rediscluster import StrictRedisCluster

logging.config.fileConfig('./logging.ini')

# startup_nodes = [{"host": "10.44.15.158", "port": "16379"}]
startup_nodes = [
    {"host": "10.51.58.229", "port": "6390"},
    {"host": "10.51.58.229", "port": "6391"},
    {"host": "10.51.58.229", "port": "6392"},
]

_start = time.time()
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
# rc = StrictRedisCluster(startup_nodes=startup_nodes)
print('use %f ms' % (time.time() - _start))


rc.set('foo', 'bar')

for i in range(1, 100):  # noqa
    try:
        logging.info("SET foo{0} {1}".format(i, i))
        rc.set("foo{0}".format(i), i+3000)
        # got = rc.get("foo{0}".format(i))
        # logging.info("GET foo{0} {1}".format(i, got))
        # time.sleep(0.5)
        # rc.set("__last__", i)
    except Exception as e:
        print("error {0}".format(e))
        sys.exit()

print('finish')
