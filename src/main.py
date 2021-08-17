import argparse
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter
from . import messages


def argparser():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        add_help=False
    )
    parser.add_argument("--name", default='all', required=False, 
                        help="Display the message from the given name",
                        choices=[x.lower() for x in messages.__all__] + ['all'])
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS)
    return parser


def main():
    args = argparser().parse_args()
    name = args.name
    all_messages = {name.lower(): messages.__dict__.get(name) for name in messages.__all__}
    if name == 'all':
        for _, tomodachi in all_messages.items():
            tomodachi().show_message()
    else:
        all_messages[name]().show_message()


if __name__ == '__main__':
    main()
