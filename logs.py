#!/usr/bin/env python3




import os
import logging
from logging import handlers
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("victor", log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=100, #10**6
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)


"""
log = logging.Logger("logs.py", logging.DEBUG)


log.debug("Msg para o dev")
log.info("Msg gerral para User")
log.warning("Msg de aviso.Não afeta RUN do programa")
log.error("Erro que afeta uma unica execução")
log.critical("Erro Geral ex : sumui DB")

print("------")

"""
try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", {str(e)})
