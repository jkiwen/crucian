import os

import click
from flask import Flask

# from site import create_app
from settings import load_settings


@click.group()
def cli():
    pass


@click.command()
def run():
    # 对运行环境进行初始化，设置flask参数
    load_settings()
    # 要求系统执行指令

    from web_site.documents import create_app

    app = create_app()
    app.run()


cli.add_command(run)

if __name__ == '__main__':
    cli()
