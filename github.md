 import logging
   import os
   for logger_name in ['snowflake.sqlalchemy', 'snowflake.connector', 'botocore']:
   for logger_name in ('snowflake.connector',):
       logger = logging.getLogger(logger_name)
       logger.setLevel(logging.DEBUG)
       ch = logging.StreamHandler()
