import click
import modules.user_module as UM
import modules.selected_subjects as SS
import modules.available_courses as AC
import modules.support.core_authenticator as CA
from bs4 import BeautifulSoup

@click.command()
@click.argument('command')
@click.argument('arg_2', default = 'false')
@click.option('--id', '-i')
@click.option('--password', '-p')
def main(command, arg_2, id, password):
    br = CA.get_context(id, password)
    raw_text = br.response().read()
    context_page = BeautifulSoup(raw_text, 'html.parser')

    if command == 'user':
        if arg_2 == 'timetable':
            click.echo(UM.get_timetable(context_page))
        else:
            click.echo(UM.get_user(context_page))
    elif command == 'courses':
        click.echo(AC.get_available_courses(context_page))
    elif command == 'subjects':
        click.echo(SS.get_selected_subjects(context_page))

if __name__ == "__main__":
    main()