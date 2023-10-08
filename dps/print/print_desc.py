class Print:
    def __init__(self) -> None:
        pass

    def print_desc(self) ->  None:
        help_message = """
        Usage: dps ARCHITECTURE

        Arguments:
        ARCHITECTURE                    Specify the architecture

        Examples:
        dps amd64
        dps arm64
        """

        print(help_message)