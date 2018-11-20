import click
import modules.user_module as UM

@click.command()
@click.argument('command')
@click.option('--id', '-i')
@click.option('--password', '-p')
def main(command, id, password):
    if command == 'user':
        click.echo(UM.get_user(id, password))

if __name__ == "__main__":
    main()

