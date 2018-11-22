import click
import modules.user_module as UM
import modules.selected_subjects as SS
import modules.available_courses as AC
import modules.support.core_authenticator as CA
from bs4 import BeautifulSoup

@click.command()
@click.argument('command')
@click.option('--id', '-i')
@click.option('--password', '-p')
def main(command, id, password):
    br = CA.get_context(id, password)
    raw_text = br.response().read()
    context_page = BeautifulSoup(raw_text, 'html.parser')

    if command == 'user':
        click.echo(UM.get_user(context_page))
    elif command == 'courses':
        click.echo(AC.get_available_courses(context_page))
    elif command == 'subjects':
        click.echo(SS.get_selected_subjects(context_page))

if __name__ == "__main__":
    main()