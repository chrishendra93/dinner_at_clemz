import messages


def main():
    all_messages = map(messages.__dict__.get, messages.__all__)
    for tomodachi in all_messages:
        tomodachi().show_message()




if __name__ == '__main__':
    main()
