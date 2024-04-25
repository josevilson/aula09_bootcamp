from sys import stderr

from loguru import logger

logger.add(sink=stderr,
           format="{time} {level} {message} {file}",
           level="INFO"
           )
logger.add('meu_app.log',
           format="{time} {level} {message} {file}",
           level="CRITICAL"
           )


def soma(x, y):
    try:
        soma = x + y
        logger.info(f'voce digitou os valores corretos {soma}')
        return soma
    except:
        logger.critical('voce tem que digitar os valores corretos.')


print(soma(1, 3))
print(soma(1, "32"))

