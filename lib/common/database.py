# -*- coding:utf-8 -*-
import pymssql
import pymysql
from lib.common.log import logger

class SqlDriver(object):
    def __init__(self, host, port, user, password, database):
        """
        initiate driver parameters
        :param host: string, ip address
        :param port: int
        :param user: string
        :param password: string
        :param database: string
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # Execute SQL Server Query
    def exec_mssql(self, sql):
        try:
            conn = pymssql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset="uft8")

            pymysql.connect()
            cur = conn.cursor()
            if cur:
                logger.info(u"Execute SQL Statement |%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    logger.warning(u"No SQL Query Data Returned")
                return rows
            else:
                logger.error(u"Failed to Connect Database")
            conn.close()
        except Exception as e:
            logger.error(e)

    # Execute MySQL Query
    def exec_mysql(self, sql):
        try:

            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset='utf8')
            cur = conn.cursor()
            if cur:
                logger.info(u"Execute SQL Statement |%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    logger.warning(u"No SQL Query Data Returned")
                return rows
            else:
                logger.error(u"Failed to Connect Database")
            conn.close()
        except Exception as e:
            logger.error(e)

    def exec_sql(self, driver, sql):
        if driver == "MYSQL":
            try:
                sql_result = SqlDriver(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database
                ).exec_mysql(sql)
                return sql_result
            except Exception as e:
                logger.error(e)

        elif driver == "MSSQL":
            try:
                sql_result = SqlDriver(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database
                ).exec_mssql(sql)
                return sql_result
            except Exception as e:
                logger.error(e)