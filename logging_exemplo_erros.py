from loguru import logger

logger.add('meu_app.log')

logger.debug('um aviso para o desenvolvedor no futuro')
logger.info('Informacao importante do processo.')
logger.warning('um aviso que vai parar no futuro')
logger.error('aconteceu um falha')
logger.critical('aconteceu uma que aborta a aplicacao.')
