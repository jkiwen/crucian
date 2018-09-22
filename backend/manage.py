import os
# from site import create_app
from settings import load_settings
from flask import Flask
import click

@click.group()
def cli():
    pass

@click.command()
def run():
    # 对运行环境进行初始化，设置flask参数
    load_settings()
    # 要求系统执行指令
    os.system('flask run')

cli.add_command(run)

if __name__ == '__main__':
    cli()