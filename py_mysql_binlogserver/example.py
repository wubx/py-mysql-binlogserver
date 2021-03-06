import logging
from py_mysql_binlogserver.server import BinlogServer


def main():
    FORMAT = "%(asctime)s %(message)s"
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    connection_settings = {
        "host": "192.168.1.100",
        "port": 3306,
        "user": "repl",
        "password": "repl1234",
        "master_id": 3306101,
        "server_id": 3306202,
        "semi_sync": True,
        "server_uuid": "a721031c-d2c1-11e9-897c-080027adb7d7",
        "heartbeat_period": 30000001024
    }
    logger.info("Start Binlog Server from %s: %s" % (connection_settings['host'], connection_settings['port']))

    try:
        server = BinlogServer(connection_settings)
        server.run()
    except KeyboardInterrupt:
        logger.info("Stop Binlog Server from %s: %s at %s %s" % (connection_settings['host'],
                                                                 connection_settings['port'],
                                                                 server._log_file,
                                                                 server._log_pos,
                                                                 ))
        server.close()


if __name__ == "__main__":
    main()
