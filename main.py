#!/usr/bin/env python3
"""
A text to speech program using gTTS

Author:     benni347@github.com
"""
from gtts import gTTS
import argparse
import sys


class Main:

    def __init__(self):
        self.verbose = False
        self.text = ""
        self.args = None

    def get_text(self):
        """
        This gets the variable text
        :return: the text object
        """
        return self.text

    def set_text(self, text: str):
        """
        This sets the text variable
        :type text: str
        :param text: the text which should be said
        """
        assert isinstance(text, str)
        self.text = text

    def main(self):
        self.parse_args()
        self.read_input()
        self.output()
    def parse_args(self):
        parser = argparse.ArgumentParser(description='A text to speech program using gTTS')

        # Add a command line argument
        parser.add_argument("-v", "--verbose",
                            help="Print more output useful for debugging",
                            action="store_true"
                            )
        parser.add_argument("-f", "--file",
                            help="The file with the content to be spoken",
                            nargs=1,
                            required=True
                            )
        parser.add_argument("-o", "--out-file",
                            help="The path to output the file like: './example.mp3' it supports multiple codecs not just mp3 via ffmpeg it gets it from the file extension so if you put './example.opus' it will still work.",
                            nargs=1,
                            required=True
                            )

        # Parse the command line arguments
        self.args = parser.parse_args()

        try:
            if self.args.help or len(sys.argv) == 1:
                # If no arguments were passed or if the --help argument was provided, print the help message and exit
                parser.print_help()
                exit()
        except AttributeError:
            pass
        try:
            if self.args.verbose:
                self.verbose = True
        except AttributeError:
            pass

    def read_input(self):
        path = self.args.file
        path = "".join(path)
        if self.args.verbose:
            print(f"The input file path is: {path}")
        try:
            with open(path, "r") as file:
                lines = [line.strip() for line in file]
                if self.verbose:
                    print(f"The list of the file content: {lines}")
                data = " ".join(lines)
                file.close()
        except FileNotFoundError:
            print("The file does not exist.")
        except IOError:
            print("An error occurred while trying to read the file.")
        if self.verbose:
            print(f"The data which will be spoken: {data}")
        self.set_text(data)

    def output(self):
        path = self.args.out_file
        path = "".join(path)
        if self.verbose:
            print(f"The output file path is: {path}")
        tts = gTTS(self.get_text())
        tts.save(path)


if __name__ == "__main__":
    main_class = Main()
    main_class.main()
